#include "CTPAPI.h"

CCTPAPI::CCTPAPI(){
	FILE *accountFile = fopen("account.in", "r");
	fscanf(accountFile, "%s\n%s\n%s\n%s\n%s\n", 
		sBrokerID,
		sInvestorID,
		sPassword,
		sAddress,
		sMarketDataPort);
 	/*strcpy(sBrokerID, "9999");
 	strcpy(sInvestorID, "041487");
 	strcpy(sPassword, "adec1202");
  	strcpy(sAddress, "180.168.146.187");
  	strcpy(sMarketDataPort, "10010");
  	strcpy(sTradePort, "10000");*/
  	nRequestID = 0;

	FILE *insListFile = fopen("insList.in", "r");
	int nNumOfIns;
	fscanf(insListFile, "%d\n", &nNumOfIns);
	for (int i = 0; i < nNumOfIns; ++i){
		char insName[100];
		fscanf(insListFile, "%s\n", insName);
		insList.push_back(insName);
		char dataFileName[100];
		sprintf(dataFileName, "%s.data", insName);
		FILE *dataFile = fopen(dataFileName, "w");
		fclose(dataFile);
	}
  
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
	if (pDepthMarketData == NULL) return;
	char filename[100];
	sprintf(filename, "%s.data", pDepthMarketData->InstrumentID);
	FILE* file = fopen(filename, "a+");
	fprintf(file, "%.3lf %.3lf %.3lf %d %d %d %.3lf %.0lf %s\n",
		pDepthMarketData->LastPrice, 
		pDepthMarketData->BidPrice1,
		pDepthMarketData->AskPrice1,
		pDepthMarketData->BidVolume1,
		pDepthMarketData->AskVolume1,
		pDepthMarketData->Volume,
		pDepthMarketData->Turnover,
		pDepthMarketData->OpenInterest,
		pDepthMarketData->UpdateTime);
	fclose(file);
}

int main(){
  CCTPAPI api;
  sleep(30000);
  return 0;
}
