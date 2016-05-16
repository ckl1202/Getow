#include "CTPAPI.h"

CCTPAPI::CCTPAPI(){
 	strcpy(sBrokerID, "9999");
 	strcpy(sInvestorID, "041487");
 	strcpy(sPassword, "adec1202");
  	strcpy(sAddress, "180.168.146.187");
  	strcpy(sMarketDataPort, "10011");
  	strcpy(sTradePort, "10010");
  	nRequestID = 0;

	insList.push_back("IF1609");
	insList.push_back("IH1609");
	insList.push_back("IC1609");
  
 	pUserApi = CThostFtdcMdApi::CreateFtdcMdApi();
 	pUserApi->RegisterSpi(this);
 	char sMarketAddress[50];
  	sprintf(sMarketAddress, "tcp://%s:%s", sAddress, sMarketDataPort);
 	pUserApi->RegisterFront(sMarketAddress);
  	pUserApi->Init();
}

CCTPAPI::~CCTPAPI(){

}

void CCTPAPI::OnFrontConnected(){
	ReqUserLogin();	
}

void CCTPAPI::ReqUserLogin(){
	CThostFtdcReqUserLoginField req;
	memset(&req, 0, sizeof(req));
	strcpy(req.BrokerID, sBrokerID);
	strcpy(req.UserID, sInvestorID);
	strcpy(req.Password, sPassword);
	int nResult = pUserApi->ReqUserLogin(&req, ++nRequestID);
	if (nResult != 0){
		cout << "Login failed\n";
		return;
	}
}

void CCTPAPI::OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin,
			CThostFtdcRspInfoField *pRspInfo,
			int nRequestID,
			bool bIsLast){
	if (!pRspUserLogin || !pRspInfo) return;
	if (pRspInfo->ErrorID != 0){
		cout << "Error: " << pRspInfo->ErrorMsg << endl;
		return;
	}
	cout << "Login successful\n";
	char **code;
	int nInsNum = insList.size();
	code = new char *[nInsNum];
	const int MAX_INS_LENGTH = 100;
	for (int i = 0;	i < nInsNum; ++i){
		code[i] = new char[MAX_INS_LENGTH];
		strcpy(code[i], insList[i].c_str());	
	}
	int nResult = pUserApi->SubscribeMarketData(code, nInsNum);
	if (0 != nResult) cout << "Subscribe instrument failed.\n";
	for (int i = 0; i < nInsNum; ++i) delete[] code[i];
	delete[] code;	
}

void CCTPAPI::OnRtnDepthMarketData(CThostFtdcDepthMarketDataField *pDepthMarketData){
	cout << pDepthMarketData->InstrumentID << endl;
}

int main(){
  CCTPAPI api;
  while(1);
  return 0;
}
