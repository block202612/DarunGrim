#pragma once
#include <windows.h>
#include "Configuration.h"
#include "DiffMachine.h"
#include "DataBaseWriter.h"

#include <string>
using namespace std;
using namespace stdext;

#define DATA_BUFSIZE 4096
#define DEFAULT_IDA_PATH TEXT( "c:\\Program Files\\IDA\\idag.exe" )

class DarunGrim
{
private:
	IDAController *pSourceController;
	IDAController *pTargetController;

	DBWrapper *pStorageDB;
	DiffMachine *pDiffMachine;
	bool OpenDatabase(char *storage_filename);
	string SourceFilename;
	string SourceIDBFilename;
	string TargetFilename;
	string TargetIDBFilename;
	bool IsLoadedSourceFile;
public:
	DarunGrim();
	~DarunGrim();

	DiffMachine *GetDiffMachine()
	{
		return pDiffMachine;
	}

	IDAController *GetSourceClientManager()
	{
		return pSourceController;
	}

	IDAController *GetTargetClientManager()
	{
		return pTargetController;
	}

	void ShowAddress(DWORD address, DWORD index)
	{
		if (index == 0)
		{
			if (pSourceController)
			{
				pSourceController->ShowAddress(address);
			}
		}
		else
		{
			if (pTargetController)
			{
				pTargetController->ShowAddress(address);
			}
		}
	}

	void ShowReverseAddress(DWORD address, DWORD index)
	{
		if (index == 1)
		{
			if (pSourceController)
			{
				pSourceController->ShowAddress(address);
			}
		}
		else
		{
			if (pTargetController)
			{
				pTargetController->ShowAddress(address);
			}
		}
	}

	char *GetSourceOrigFilename()
	{
		if (pSourceController)
		{
			char *filename = pSourceController->GetOriginalFilePath();
		}
		return NULL;
	}

	char *GetTargetOrigFilename()
	{
		if (pTargetController)
		{
			return pTargetController->GetOriginalFilePath();
		}
		return NULL;
	}

	list <BLOCK> GetSourceAddresses(DWORD address)
	{
		return pSourceController->GetFunctionMemberBlocks(address);
	}

	list <BLOCK> GetTargetAddresses(DWORD address)
	{
		return pTargetController->GetFunctionMemberBlocks(address);
	}

	void SetLogParameters( int ParamLogOutputType, int ParamDebugLevel, const char *LogFile = NULL );

	bool AcceptIDAClientsFromSocket( const char *storage_filename = NULL );
	
	void ListDiffDatabase(const char *storage_filename);
	bool Load( const char *storage_filename );

	bool PerformDiff();
	bool PerformDiff(const char *src_storage_filename, DWORD source_address, const char *target_storage_filename, DWORD target_address, const char *output_storage_filename);


	bool ShowOnIDA();

	const char *GetSourceFilename();
	const char *GetSourceIDBFilename();
	void SetSourceFilename( char *source_filename );
	const char *GetTargetFilename();
	const char *GetTargetIDBFilename();
	void SetTargetFilename( char *target_filename );
	bool LoadedSourceFile();
	void SetLoadedSourceFile( bool is_loaded );

	void ShowAddresses( unsigned long source_address, unsigned long target_address );
	void ColorAddress( int index, unsigned long start_address, unsigned long end_address,unsigned long color );

private:
	DBWrapper *m_OutputDB;
	unsigned short ListeningPort;
	SOCKET ListeningSocket;
	IDAController *IDAControllers[2];

	char *IDAPath;
	DWORD IDACommandProcessorThreadId;
	char IDALogFilename[MAX_PATH + 1];

	bool GenerateIDALogFilename();
	char *EscapeFilename(char *filename);
	char *LogFilename;
public:

	void SetDatabase(DBWrapper *OutputDB);
	bool StartIDAListener(unsigned short port);
	bool StopIDAListener();

	IDAController *GetIDAControllerFromFile(char *DataFile);
	DWORD SetMembers(DiffMachine *pArgDiffMachine);
	DWORD IDACommandProcessor();
	BOOL CreateIDACommandProcessorThread();
	void SetIDAPath(const char *ParamIDAPath);
	void SetLogFilename(char *logfilename)
	{
		LogFilename = EscapeFilename(logfilename);
	}
	void GenerateSourceDGFFromIDA(char *output_filename, char *log_filename);
	void GenerateTargetDGFFromIDA(char *output_filename, char *log_filename);
	void GenerateDGFFromIDA(const char *ida_filename, unsigned long StartAddress, unsigned long EndAddress, char *output_filename, char *log_filename);
	void ConnectToDarunGrim(const char *ida_filename);
	void SetIDALogFilename(const char *ida_log_filename);
	const char *GetIDALogFilename();
	BOOL AcceptIDAClient(IDAController *pIDAController, bool RetrieveData);
};
