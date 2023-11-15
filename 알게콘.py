from datetime import datetime, timedelta

from pykrx import stock
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_finance import candlestick2_ohlc

market = 'KOSPI'  # KOSPI, KOSDAQ, KONEX 중 타깃 시장 지정 (StockInfo 클래스의 get_tickers 메소드에서 사용)


class StockInfo:
    def __init__(self):
        print('프로그램 구동에 필요한 주식 정보를 불러오는 중입니다... 잠시만 기다려 주세요!')
        self.__tickers: list = self.__get_tickers()
        self.__firms: pd.DataFrame = self.__get_firms(self.__tickers)

    def __get_tickers(self):
        today_ymd = datetime.today().strftime('%Y%m%d')
        tickers: list = stock.get_market_ticker_list(today_ymd, market=market)
        return tickers

    def __get_firms(self, tickers: list):
        firm_names_list: list = []
        for ticker in tickers:
            firm_names_list.append(stock.get_market_ticker_name(ticker))

        temp_firm_names = {
            'firm_name': firm_names_list
        }
        firm_names_df: pd.DataFrame = pd.DataFrame(temp_firm_names, index=tickers)

        return firm_names_df

    def _search_firm(self, keyword: str):
        matching_results: list = list(self.__firms.index[self.__firms['firm_name'].str.contains(keyword)])  # self.__firms에서 검색어가 포함된 회사의 티커를 반환
        if len(matching_results) > 0:
            return matching_results
        else:
            return False

    def _get_firm_ohlcv(self, target_firm_ticker, before_date):
        start_date = (datetime.now() - timedelta(days=int(before_date))).strftime('%Y%m%d')
        today_date = datetime.now().strftime('%Y%m%d')
        target_firm_ohlcv: pd.DataFrame = stock.get_market_ohlcv(start_date, today_date, target_firm_ticker)
        return target_firm_ohlcv

    def _get_ticker_fundamental(self, target_firm_ticker, date):
        target_firm_fundamental: pd.DataFrame = stock.get_market_fundamental(date, date, target_firm_ticker)
        return target_firm_fundamental


class DataVisualizer:
    def _draw_ohlcv(self, ticker: str, ohlcv_df: pd.DataFrame):
        date_list = []
        for date in ohlcv_df.index.tolist():
            date_list.append(str(date).replace('-', '')[2:8])

        # make data lists
        open_price_list = ohlcv_df.loc[:, ['시가']].values.flatten().tolist()
        close_price_list = ohlcv_df.loc[:, ['종가']].values.flatten().tolist()
        low_price_list = ohlcv_df.loc[:, ['저가']].values.flatten().tolist()
        high_price_list = ohlcv_df.loc[:, ['고가']].values.flatten().tolist()
        volume_list = ohlcv_df.loc[:, ['거래량']].values.flatten().tolist()

        # set initial figures
        fig = plt.figure(figsize=(10, 5))
        fig.set_facecolor('w')
        gs = gridspec.GridSpec(2, 1, height_ratios=[3, 1])
        axes = []
        axes.append(plt.subplot(gs[0]))
        axes.append(plt.subplot(gs[1], sharex=axes[0]))
        axes[0].get_xaxis().set_visible(False)

        ohlc = [open_price_list, high_price_list, low_price_list, close_price_list]

        # candlestick chart
        candlestick2_ohlc(axes[0], open_price_list, high_price_list, low_price_list, close_price_list, width=1,
                          colorup='r', colordown='b')
        axes[0].get_yaxis().set_major_formatter(
            matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))  # 천 단위 콤마 구별

        # trading volume chart
        axes[1].bar(date_list, volume_list, color='k', width=0.6, align='center')
        axes[1].get_yaxis().set_major_formatter(
            matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))  # 천 단위 콤마 구별

        # set other plt options
        current_values = plt.gca().get_yticks()
        plt.gca().set_yticklabels(['{:.0f}'.format(x) for x in current_values])
        fig.suptitle(f'{stock.get_market_ticker_name(ticker)} ({ticker})')
        plt.xlabel(f'조회기간: {date_list[0]}~{date_list[-1]}, 가격단위: 대한민국 원(KRW)')
        plt.xticks(rotation=60)
        plt.tight_layout()
        plt.show()


class StockRecommender(StockInfo, DataVisualizer):
    def __init__(self):
        super().__init__()
        self.ticker, self.ohlcv_data = self.__get_user_input()
        self.__show_stock_graph()
        self.__show_fundamental()

    def __get_user_input(self):
        while True:
            keyword_to_search: str = input('검색하고자 하는 기업의 이름을 입력하세요: ')
            temp_firms_tickers = super()._search_firm(keyword_to_search)
            if temp_firms_tickers:  # 검색 결과 존재시
                while True:
                    temp_firms_names: list = [stock.get_market_ticker_name(ticker) for ticker in temp_firms_tickers]

                    if len(temp_firms_tickers) == 1:
                        break

                    # 정확히 일치하는 문자열이 있다면, 검색 결과 포함 확인 전에 while문 탈출
                    is_exact_match = False
                    for firm_name in temp_firms_names:
                        if keyword_to_search == firm_name:
                            is_exact_match = True
                            break
                    if is_exact_match: break

                    # 정확히 일치하는 문자열이 없을 경우 검색 결과들을 표시
                    print('검색 결과: ', *temp_firms_names)
                    keyword_to_search = input('검색 결과가 많습니다. 검색 결과 중 하나의 키워드를 입력하세요: ')

                    # 검색 결과에 입력 문자열이 포함되는지 확인 후 맞다면 재검색
                    if keyword_to_search in temp_firms_names:
                        temp_firms_tickers = super()._search_firm(keyword_to_search)
                        if len(temp_firms_tickers) == 1:
                            break
                    else:
                        print('검색 결과 중 하나의 기업명을 입력해 주세요.')
                print(f'{stock.get_market_ticker_name(temp_firms_tickers[0])}의 주가정보를 조회합니다.')
                while True:
                    date_input = input('조회하려는 기간의 날수(일 단위)를 입력하세요(ex: 30): ')
                    if date_input.isdigit():
                        before_date = int(date_input)
                        break
                    else:
                        print('잘못된 입력입니다. 다시 입력해 주세요.')
                return temp_firms_tickers[0], super()._get_firm_ohlcv(temp_firms_tickers[0], before_date)  # 기업 티커, 주식정보 데이터프레임을 묶은 튜플
            else:
                print('검색 결과가 없습니다. 다시 입력해 주세요.')

    def __show_stock_graph(self):
        super()._draw_ohlcv(self.ticker, self.ohlcv_data)
        start_date = str(self.ohlcv_data.index.tolist()[0]).replace('-', '')[2:8]
        end_date = str(self.ohlcv_data.index.tolist()[-1]).replace('-', '')[2:8]
        print(f'{stock.get_market_ticker_name(self.ticker)}의 {start_date}~{end_date}간 주가 정보가 표시되었습니다.')

    def __show_fundamental(self):
        print(f'{stock.get_market_ticker_name(self.ticker)}의 최근 영업일자 BPS/PER/PBR/EPS/DIV/DPS 조회정보는 아래와 같습니다.')
        print(super()._get_ticker_fundamental(self.ticker, str(self.ohlcv_data.index.tolist()[-1])))


StockRecommender()
