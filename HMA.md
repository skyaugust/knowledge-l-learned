# Hcicloud MicArray SDK

svn checkout http://cvs:8080/svn/HCICloud/develop/trunk/projects/HMA3.0

hci_micarray.hci_micarray_session_start
    MicArrayHandler.Start
        DataPcmSaver.Start() in new thread
        OutPutTask.Start() in new thread
        WakeTask.Start() in new thread
        DBFTask.Start() in new thread
        AECTask.Start() in new thread run AECTask.Process()

VoiceData Producer:
MicArrayHandler.DoProcess(micData, refData)
AECTask.AddData to AECTask.VoiceQueue(micData,refData)

VoiceData consumer:
AECTask.Process read <micData, refData> from AECTask.VoiceQueue
    AECTASK.ProcessDen
        VQEHelper.ProcessDen
            iSpeakVQE_SessionProcess
            return pDenBuffer
        return pDenBuffer as aecOutData
        MicArrayHandler.OnAECDataProcesed(aecOutData, micData)
            DBFTask.AddData(aecOutData, micData)
            WakeTask.AddData(aecOutData, micData)
            