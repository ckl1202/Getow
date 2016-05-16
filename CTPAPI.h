#include "ThostFtdcMdApi.h"
#include <string.h>
#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class CCTPAPI : public CThostFtdcMdSpi{
private:
	char sBrokerID[30];
	char sInvestorID[30];
	char sPassword[30];
	char sAddress[20];
	char sMarketDataPort[10];
	char sTradePort[10];
	int nRequestID;

	CThostFtdcMdApi* pUserApi;

	vector<string> insList;
  
public:
	CCTPAPI();
	~CCTPAPI();
	void OnFrontConnected();
	void ReqUserLogin();
	void OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin,
			CThostFtdcRspInfoField *pRspInfo,
			int nRequestID,
			bool bIsLast);
	void OnRtnDepthMarketData(CThostFtdcDepthMarketDataField *pDepthMarketData);
};
