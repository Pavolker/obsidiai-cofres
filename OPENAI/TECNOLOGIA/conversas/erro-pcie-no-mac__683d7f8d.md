---
source: DATAGPT
conversation_id: 683d7f8d-10ac-8002-8e66-338e67ed13e7
title: "Erro PCIe no Mac"
theme: TECNOLOGIA
created: 2025-06-02T10:40:13.322005Z
message_count: 2
attachments_count: 0
---

# Erro PCIe no Mac

- Tema: `TECNOLOGIA`
- Conversation ID: `683d7f8d-10ac-8002-8e66-338e67ed13e7`

## Transcrição

### user

Meu computador desligou subtamente e gerou o relatorio de erro abaixo. O que significa isso ?

"
panic(cpu 3 caller 0xfffffe0013823d64): "apcie[2:lan-1gb]::_linkDownInterrupt: Unexpected link down linksts=0xa9000208 pcielint=0x00004000 linkcdmsts=0x00000000 (ltssm 0x0=DETECT_QUIET)\\n" @AppleT811xPCIePort.cpp:1644
Debugger message: panic
Memory ID: 0x6
OS release type: User
OS version: 24F74
Kernel version: Darwin Kernel Version 24.5.0: Tue Apr 22 19:54:26 PDT 2025; root:xnu-11417.121.6~2/RELEASE_ARM64_T8112
Fileset Kernelcache UUID: 15601AA8C686B692A4CE5A6782B05569
Kernel UUID: 3E4B2638-BBC1-36F7-BEE0-D2E41D599E88
Boot session UUID: A087053F-DA9A-4469-AA30-3931DCD5A2A6
iBoot version: iBoot-11881.121.1
iBoot Stage 2 version: iBoot-11881.121.1
secure boot?: YES
roots installed: 0
Paniclog version: 14
KernelCache slide: 0x0000000009570000
KernelCache base:  0xfffffe0010574000
Kernel slide:      0x0000000009578000
Kernel text base:  0xfffffe001057c000
Kernel text exec slide: 0x000000000acf4000
Kernel text exec base:  0xfffffe0011cf8000
mach_absolute_time: 0x63e933968
Epoch Time:        sec       usec
  Boot    : 0x683d7a48 0x000e5519
  Sleep   : 0x00000000 0x00000000
  Wake    : 0x00000000 0x00000000
  Calendar: 0x683d7ea1 0x000668c2

Zone info:
  Zone map: 0xfffffe110c000000 - 0xfffffe370c000000
  . VM    : 0xfffffe110c000000 - 0xfffffe16d8000000
  . RO    : 0xfffffe16d8000000 - 0xfffffe1972000000
  . GEN0  : 0xfffffe1972000000 - 0xfffffe1f3e000000
  . GEN1  : 0xfffffe1f3e000000 - 0xfffffe250a000000
  . GEN2  : 0xfffffe250a000000 - 0xfffffe2ad6000000
  . GEN3  : 0xfffffe2ad6000000 - 0xfffffe30a2000000
  . DATA  : 0xfffffe30a2000000 - 0xfffffe370c000000
  Metadata: 0xfffffe4d84010000 - 0xfffffe4d8d810000
  Bitmaps : 0xfffffe4d8d810000 - 0xfffffe4d8ee1c000
  Extra   : 0 - 0

CORE 0 recently retired instr at 0xfffffe0011ebace0
CORE 1 recently retired instr at 0xfffffe0011ebace0
CORE 2 recently retired instr at 0xfffffe0011ebace0
CORE 3 recently retired instr at 0xfffffe0011eb944c
CORE 4 recently retired instr at 0xfffffe0011ebace0
CORE 5 recently retired instr at 0xfffffe0011ebace0
CORE 6 recently retired instr at 0xfffffe0011ebace0
CORE 7 recently retired instr at 0xfffffe0011ebace0
TPIDRx_ELy = {1: 0xfffffe1974044790  0: 0x0000000000000003  0ro: 0x0000000000000000 }
CORE 0 PVH locks held: None
CORE 1 PVH locks held: None
CORE 2 PVH locks held: None
CORE 3 PVH locks held: None
CORE 4 PVH locks held: None
CORE 5 PVH locks held: None
CORE 6 PVH locks held: None
CORE 7 PVH locks held: None
CORE 0: PC=0xfffffe0011d08c38, LR=0xfffffe0011d08c38, FP=0x0000000000000000
CORE 1: PC=0x000000011b97bdf8, LR=0x000000011df0a810, FP=0x000000016bb8dca0
CORE 2: PC=0xfffffe0011d721f8, LR=0xfffffe001225067c, FP=0xfffffe647ff3bbb0
CORE 3 is the one that panicked. Check the full backtrace for details.
CORE 4: PC=0xfffffe00127e6658, LR=0xfffffe00128104cc, FP=0xfffffe647e6bba30
CORE 5: PC=0xfffffe001261f1d0, LR=0xfffffe001261afe8, FP=0xfffffe00178ebd80
CORE 6: PC=0xfffffe0011d90fe4, LR=0xfffffe0011d90fe4, FP=0xfffffe647e073ed0
CORE 7: PC=0xfffffe0011d90fe8, LR=0xfffffe0011d90fe4, FP=0xfffffe64801e7ed0
Compressor Info: 10% of compressed pages limit (OK) and 9% of segments limit (OK) with 1 swapfiles and OK swap space
Panicked task 0xfffffe29d5fab940: 0 pages, 563 threads: pid 0: kernel_task
Panicked thread: 0xfffffe1974044790, backtrace: 0xfffffe647feeb6c0, tid: 255
		  lr: 0xfffffe0011d54ae0  fp: 0xfffffe647feeb750
		  lr: 0xfffffe0011eb1598  fp: 0xfffffe647feeb7c0
		  lr: 0xfffffe0011eaf794  fp: 0xfffffe647feeb880
		  lr: 0xfffffe0011cff8c0  fp: 0xfffffe647feeb890
		  lr: 0xfffffe0011d543d8  fp: 0xfffffe647feebc60
		  lr: 0xfffffe00125ddbf4  fp: 0xfffffe647feebc80
		  lr: 0xfffffe0013823d64  fp: 0xfffffe647feebd40
		  lr: 0xfffffe0012eb3260  fp: 0xfffffe647feebd60
		  lr: 0xfffffe0012eadc94  fp: 0xfffffe647feebe40
		  lr: 0xfffffe00124da544  fp: 0xfffffe647feebe80
		  lr: 0xfffffe00124d6568  fp: 0xfffffe647feebed0
		  lr: 0xfffffe00124d7158  fp: 0xfffffe647feebf20
		  lr: 0xfffffe0011d08c48  fp: 0x0000000000000000
      Kernel Extensions in backtrace:
         com.apple.driver.AppleEmbeddedPCIE(1.0)[0B3B580D-98BD-38CF-B435-B91EA38FF0F0]@0xfffffe0012ea35e0->0xfffffe0012eba45b
            dependency: com.apple.driver.AppleARMPlatform(1.0.2)[17D2041F-0EDE-3553-AF18-4A5DF8862B30]@0xfffffe0012780e10->0xfffffe00127d6e2f
            dependency: com.apple.driver.ApplePIODMA(1)[6E3DD348-687E-37E6-A6EC-B84234C5DC39]@0xfffffe001348fe70->0xfffffe0013494733
            dependency: com.apple.driver.IODARTFamily(1)[96BFE781-06B9-3EAE-B1A2-B37F524D9075]@0xfffffe00142ed4b0->0xfffffe001430172f
            dependency: com.apple.iokit.IOPCIFamily(2.9)[7E6672DD-F880-3B24-A0F9-C39A7F79FA46]@0xfffffe0014677640->0xfffffe00146a8763
            dependency: com.apple.iokit.IOReportFamily(47)[7CE55C92-8D7B-3857-B41C-B8A897DCC039]@0xfffffe00146b17a0->0xfffffe00146b4657
         com.apple.driver.AppleT8112PCIe(1.0)[7AFC049A-8EBC-3031-A08F-634289536312]@0xfffffe001381fbf0->0xfffffe00138279f7
            dependency: com.apple.driver.AppleARMPlatform(1.0.2)[17D2041F-0EDE-3553-AF18-4A5DF8862B30]@0xfffffe0012780e10->0xfffffe00127d6e2f
            dependency: com.apple.driver.AppleEmbeddedPCIE(1)[0B3B580D-98BD-38CF-B435-B91EA38FF0F0]@0xfffffe0012ea35e0->0xfffffe0012eba45b
            dependency: com.apple.iokit.IOPCIFamily(2.9)[7E6672DD-F880-3B24-A0F9-C39A7F79FA46]@0xfffffe0014677640->0xfffffe00146a8763
            dependency: com.apple.iokit.IOReportFamily(47)[7CE55C92-8D7B-3857-B41C-B8A897DCC039]@0xfffffe00146b17a0->0xfffffe00146b4657

last started kext at 3530862046: com.apple.filesystems.smbfs	6.0 (addr 0xfffffe001115d280, size 111737)
loaded kexts:
com.apple.filesystems.smbfs	6.0
com.apple.filesystems.autofs	3.0
com.apple.driver.CoreKDL	1
com.apple.driver.AppleBiometricServices	1
com.apple.iokit.SCSITaskUserClient	500.120.2
com.apple.driver.AppleUSBMassStorageInterfaceNub	556
com.apple.driver.AppleAOPVoiceTrigger	440.4
com.apple.iokit.AppleBCM5701Ethernet	11.0.0
com.apple.driver.DiskImages.ReadWriteDiskImage	493.0.0
com.apple.driver.DiskImages.UDIFDiskImage	493.0.0
com.apple.driver.DiskImages.RAMBackingStore	493.0.0
com.apple.driver.DiskImages.FileBackingStore	493.0.0
com.apple.driver.SEPHibernation	1
com.apple.driver.AppleSmartBatteryManager	161.0.0
com.apple.driver.AppleUSBDeviceNCM	5.0.0
com.apple.driver.AppleThunderboltIP	4.0.3
com.apple.driver.AppleFileSystemDriver	3.0.1
com.apple.nke.l2tp	1.9
com.apple.filesystems.tmpfs	1
com.apple.filesystems.nfs	1
com.apple.filesystems.lifs	1
com.apple.filesystems.apfs	2332.120.31
com.apple.IOTextEncryptionFamily	1.0.0
com.apple.filesystems.hfs.kext	683.120.3
com.apple.security.BootPolicy	1
com.apple.BootCache	40
com.apple.AppleFSCompression.AppleFSCompressionTypeZlib	1.0.0
com.apple.AppleFSCompression.AppleFSCompressionTypeDataless	1.0.0d1
com.apple.driver.AppleSmartIO2	1
com.apple.driver.ApplePMP	1
com.apple.AGXG14G	327.5
com.apple.driver.AppleSN012776Amp	840.26
com.apple.driver.AppleProResHW	475.6
com.apple.driver.AppleAVE2	803.71.1
com.apple.driver.AppleAVD	863.1
com.apple.AppleEmbeddedSimpleSPINORFlasher	1
com.apple.driver.AppleCS42L84Audio	840.26
com.apple.driver.AppleSamsungSerial	1.0.0d1
com.apple.driver.ApplePMPFirmware	1
com.apple.driver.AppleMobileDispH14G-DCP	140.0
com.apple.driver.AppleSPIMC	1
com.apple.driver.AppleTypeCRetimer	1.0.0
com.apple.driver.usb.AppleSynopsysUSB40XHCI	1
com.apple.driver.AudioDMAController-T8112	450.4
com.apple.driver.AppleJPEGDriver	7.6.8
com.apple.driver.AppleSerialShim	1
com.apple.driver.AppleT8020SOCTuner	1
com.apple.driver.AppleT8112CLPC	1
com.apple.driver.AppleEventLogHandler	1
com.apple.driver.AppleS5L8960XNCO	1
com.apple.driver.AppleT8112PMGR	1
com.apple.driver.AppleS8000AES	1
com.apple.driver.AppleS5L8920XPWM	1.0.0d1
com.apple.driver.AppleS8000DWI	1.0.0d1
com.apple.driver.AppleInterruptControllerV2	1.0.0d1
com.apple.driver.AppleBluetoothModule	1
com.apple.driver.AppleBCMWLANBusInterfacePCIe	1
com.apple.driver.AppleT8110DART	1
com.apple.driver.AppleS5L8940XI2C	1.0.0d2
com.apple.driver.AppleM68Buttons	1.0.0d1
com.apple.driver.AppleT8110	1
com.apple.iokit.IOUserEthernet	1.0.1
com.apple.driver.usb.AppleUSBUserHCI	1
com.apple.iokit.IOKitRegistryCompatibility	1
com.apple.iokit.EndpointSecurity	1
com.apple.driver.AppleDiskImages2	385.120.4
com.apple.AppleSystemPolicy	2.0.0
com.apple.kec.InvalidateHmac	1
com.apple.kec.AppleEncryptedArchive	1
com.apple.driver.driverkit.serial	6.0.0
com.apple.driver.AppleMesaSEPDriver	100.99
com.apple.iokit.IOBiometricFamily	1
com.apple.driver.usb.IOUSBHostHIDDevice	1.2
com.apple.driver.usb.cdc.ecm	5.0.0
com.apple.driver.usb.cdc.acm	5.0.0
com.apple.driver.usb.serial	6.0.0
com.apple.driver.usb.cdc	5.0.0
com.apple.driver.AppleUSBAudio	750.4
com.apple.iokit.IOAudioFamily	600.2
com.apple.vecLib.kext	1.2.0
com.apple.driver.AppleUVDMDriver	1.0.0
com.apple.driver.AppleUVDM	1.0.0
com.apple.driver.AppleAOPAudio	440.12
com.apple.driver.usb.AppleEmbeddedUSBXHCIPCI	1
com.apple.driver.usb.AppleUSBXHCIPCI	1.2
com.apple.driver.AppleConvergedIPCOLYBTControl	1
com.apple.driver.AppleConvergedPCI	1
com.apple.driver.AppleBluetoothDebug	1
com.apple.driver.DiskImages.KernelBacked	493.0.0
com.apple.driver.AppleSEPHDCPManager	1.0.1
com.apple.driver.AppleTrustedAccessory	1
com.apple.iokit.AppleSEPGenericTransfer	1
com.apple.driver.AppleBTM	1.0.1
com.apple.driver.AppleXsanScheme	3
com.apple.driver.usb.networking	5.0.0
com.apple.driver.AppleThunderboltDPInAdapter	8.5.1
com.apple.driver.AppleThunderboltDPAdapterFamily	8.5.1
com.apple.driver.AppleThunderboltPCIDownAdapter	4.1.1
com.apple.driver.AppleThunderboltUSBDownAdapter	1.0.4
com.apple.nke.ppp	1.9
com.apple.driver.AppleBSDKextStarter	3
com.apple.kext.triggers	1.0
com.apple.driver.IOHIDPowerSource	1
com.apple.driver.AppleCallbackPowerSource	1
com.apple.filesystems.hfs.encodings.kext	1
com.apple.driver.AppleSyntheticGameController	12.5.3
com.apple.driver.AppleDCPDPTXProxy	1.0.0
com.apple.driver.DCPDPFamilyProxy	1
com.apple.driver.AppleStockholmControl	1.0.0
com.apple.AGXFirmwareKextG14GRTBuddy	1
com.apple.AGXFirmwareKextRTBuddy64	327.5
com.apple.driver.AppleDiagnosticDataAccessReadOnly	1.0.0
com.apple.driver.AppleH11ANEInterface	8.600.2
com.apple.iokit.IONVMeFamily	2.1.0
com.apple.driver.AppleNANDConfigAccess	1.0.0
com.apple.iokit.IOGPUFamily	104.5
com.apple.driver.AppleSPU	1
com.apple.driver.AppleMCA2-T8112	940.3
com.apple.driver.AppleCSEmbeddedAudio	840.26
com.apple.driver.AppleEmbeddedAudio	840.26
com.apple.iokit.AppleARMIISAudio	440.17
com.apple.driver.IISAudioIsolatedStreamECProxy	440.17
com.apple.driver.ExclavesAudioKext	240.34
com.apple.driver.AppleEmbeddedAudioLibs	420.3
com.apple.driver.DCPAVFamilyProxy	1
com.apple.driver.AppleHPM	3.4.4
com.apple.iokit.IOMobileGraphicsFamily-DCP	343.0.0
com.apple.driver.AppleDCP	1
com.apple.driver.AppleFirmwareKit	1
com.apple.driver.AppleFirmwareUpdateKext	1
com.apple.iokit.IOMobileGraphicsFamily	343.0.0
com.apple.driver.AppleUSBXDCIARM	1.0
com.apple.driver.AppleUSBXDCI	1.0
com.apple.iokit.IOUSBDeviceFamily	2.0.0
com.apple.driver.AppleT8112TypeCPhy	1
com.apple.driver.AppleT8103TypeCPhy	1
com.apple.driver.AppleSPMIPMU	1.0.1
com.apple.driver.AppleDialogPMU	1.0.1
com.apple.driver.usb.AppleSynopsysUSBXHCI	1
com.apple.driver.usb.AppleUSBXHCI	1.2
com.apple.driver.AppleEmbeddedUSBHost	1
com.apple.driver.usb.AppleUSBHub	1.2
com.apple.driver.usb.AppleUSBHostCompositeDevice	1.2
com.apple.driver.AppleM2ScalerCSCDriver	265.0.0
com.apple.driver.AppleSPMI	1.0.1
com.apple.driver.ApplePassthroughPPM	3.0
com.apple.driver.AppleSART	1
com.apple.driver.ApplePMGR	1
com.apple.driver.AppleA7IOP-ASCWrap-v4	1.0.2
com.apple.driver.AppleARMWatchdogTimer	1
com.apple.driver.AppleT8112PCIe	1
com.apple.driver.AppleA7IOP-MXWrap-v1	1.0.2
com.apple.driver.usb.AppleUSBHostPacketFilter	1.0
com.apple.driver.AppleT8103PCIeCPIODMA	1
com.apple.driver.AppleThunderboltNHI	7.2.81
com.apple.driver.AppleDisplayCrossbar	1.0.0
com.apple.iokit.IODisplayPortFamily	1.0.0
com.apple.driver.AppleTypeCPhy	1
com.apple.driver.AppleT8103PCIeC	1
com.apple.iokit.IOThunderboltFamily	9.3.3
com.apple.iokit.IOPortFamily	1.0
com.apple.driver.AppleBluetoothDebugService	1
com.apple.driver.AppleBCMWLANCore	1.0.0
com.apple.iokit.IO80211Family	1200.13.1
com.apple.driver.IOImageLoader	1.0.0
com.apple.driver.AppleOLYHAL	1
com.apple.iokit.IOAVBFamily	1320.3
com.apple.plugin.IOgPTPPlugin	1340.12
com.apple.driver.AppleGPIOICController	1.0.2
com.apple.driver.AppleMobileApNonce	1
com.apple.driver.AppleFireStormErrorHandler	1
com.apple.driver.AppleMultiFunctionManager	1
com.apple.driver.corecapture	1.0.4
com.apple.driver.AppleEmbeddedPCIE	1
com.apple.driver.ApplePIODMA	1
com.apple.iokit.IOTimeSyncFamily	1340.12
com.apple.driver.DiskImages	493.0.0
com.apple.iokit.IOGraphicsFamily	599
com.apple.iokit.IOBluetoothFamily	9.0.0
com.apple.driver.AppleUIO	1
com.apple.driver.AppleSSE	1.0
com.apple.driver.AppleSEPKeyStore	2
com.apple.driver.AppleUSBTDM	556
com.apple.iokit.IOUSBMassStorageDriver	259.100.1
com.apple.iokit.IOPCIFamily	2.9
com.apple.iokit.IOUSBHostFamily	1.2
com.apple.driver.AppleUSBHostMergeProperties	1.2
com.apple.driver.usb.AppleUSBCommon	1.0
com.apple.driver.AppleSMC	3.1.9
com.apple.driver.RTBuddy	1.0.0
com.apple.driver.AppleEmbeddedTempSensor	1.0.0
com.apple.driver.AppleARMPMU	1.0
com.apple.iokit.IOAccessoryManager	1.0.0
com.apple.driver.AppleOnboardSerial	1.0
com.apple.iokit.IOSerialFamily	11
com.apple.iokit.IOSCSIBlockCommandsDevice	500.120.2
com.apple.iokit.IOSCSIArchitectureModelFamily	500.120.2
com.apple.driver.AppleRSMChannel	1
com.apple.iokit.IORSMFamily	1
com.apple.driver.AppleLockdownMode	1
com.apple.driver.AppleIPAppender	1.0
com.apple.iokit.IOSkywalkFamily	1.0
com.apple.driver.mDNSOffloadUserClient	1.0.1b8
com.apple.iokit.IONetworkingFamily	3.4
com.apple.driver.AppleFDEKeyStore	28.30
com.apple.driver.AppleEffaceableStorage	1.0
com.apple.driver.AppleCredentialManager	1.0
com.apple.driver.AppleSEPManager	1.0.1
com.apple.driver.IODARTFamily	1
com.apple.driver.AppleA7IOP	1.0.2
com.apple.driver.IOSlaveProcessor	1
com.apple.driver.AppleBiometricSensor	2
com.apple.iokit.IOHIDFamily	2.0.0
com.apple.AUC	1.0
com.apple.iokit.IOSurface	372.5.2
com.apple.iokit.IOAVFamily	1.0.0
com.apple.iokit.IOHDCPFamily	1.0.0
com.apple.iokit.IOCECFamily	1
com.apple.iokit.IOAudio2Family	1.0
com.apple.driver.AppleIISController	440.2
com.apple.driver.AppleAudioClockLibs	420.3
com.apple.driver.FairPlayIOKit	72.13.0
com.apple.driver.AppleARMPlatform	1.0.2
com.apple.iokit.IOSlowAdaptiveClockingFamily	1.0.0
com.apple.iokit.IOReportFamily	47
com.apple.security.quarantine	4
com.apple.security.sandbox	300.0
com.apple.iokit.IOStorageFamily	2.1
com.apple.kext.AppleMatch	1.0.0d1
com.apple.driver.AppleMobileFileIntegrity	1.0.5
com.apple.iokit.CoreAnalyticsFamily	1
com.apple.security.AppleImage4	7.0.0
com.apple.kext.CoreTrust	1
com.apple.iokit.IOCryptoAcceleratorFamily	1.0.1
com.apple.kec.pthread	1
com.apple.kec.Libm	1
com.apple.kec.Compression	1.0
com.apple.kec.corecrypto	14.0



** Stackshot Succeeded ** Bytes Traced 507732 (Uncompressed 1208960) **

"

### assistant

Paulo, o relatório que você compartilhou é um **panic log** do macOS — um tipo de erro crítico no sistema operacional que faz o computador reiniciar automaticamente para proteger o hardware ou o próprio sistema. Abaixo está uma explicação técnica, mas sintética, sobre o que aconteceu com base nas informações fornecidas:

---

### **Diagnóstico do erro**

#### **1. Tipo de erro:**
```
panic(cpu 3 caller 0xfffffe0013823d64): 
"apcie[2:lan-1gb]::_linkDownInterrupt: Unexpected link down"
```

Esse trecho indica que houve uma **falha inesperada no barramento PCIe** (Peripheral Component Interconnect Express), mais especificamente no componente de rede (“lan-1gb” = conexão de rede Ethernet 1 gigabit). O sistema detectou que o **link de comunicação PCIe foi interrompido de forma abrupta**, o que não deveria ocorrer.

#### **2. Causa provável:**
A falha está associada ao driver da Apple para portas PCIe (linha relevante):
```
com.apple.driver.AppleEmbeddedPCIE
```

Em especial, no componente `AppleT8112PCIe`, que é relacionado ao **chip Apple Silicon T8112**, utilizado em Macs mais recentes (provavelmente um Mac com M2 ou equivalente).

O estado `ltssm = DETECT_QUIET` indica que o link físico PCIe está em um **estado de detecção silenciosa**, ou seja, o hardware deixou de responder como esperado durante uma operação normal.

---

### **Causas possíveis:**

1. **Erro de hardware intermitente**
   - Problema físico no controlador PCIe integrado (por exemplo, falha temporária no chip de rede onboard).
   - Falha de energia momentânea ou interferência elétrica.

2. **Problema com driver/kernel**
   - Bug no driver do sistema responsável pela comunicação PCIe.
   - Incompatibilidade introduzida por uma **atualização recente do macOS** (você está usando a versão 24F74).

3. **Conflito com periféricos**
   - Algum periférico conectado via Thunderbolt/USB-C pode ter causado instabilidade na controladora PCIe.
   - Problemas com hubs, adaptadores de rede ou armazenamento externos.

---

### **Consequência imediata:**
O sistema operacional, ao detectar esse erro no nível do kernel, acionou o mecanismo de **"kernel panic"**, forçando um reinício de emergência para evitar corrupção de dados ou danos ao hardware.

---

### **Recomendações:**

#### **1. Se foi um evento isolado:**
- Observe se o problema volta a ocorrer.
- Atualize o macOS para a versão mais recente, caso esteja disponível.

#### **2. Se o problema se repetir:**
- Reinicie o Mac em **modo de segurança** (`Shift` pressionado ao iniciar).
- Verifique se há periféricos conectados (cabos, hubs, docks) e teste o sistema sem eles.
- Execute um **Apple Diagnostics**: desligue o Mac, ligue novamente e pressione `D`.
- Considere levar o equipamento a uma **assistência autorizada**, pois pode haver falha de hardware no controlador PCIe.

---

Se quiser, posso ajudá-lo a montar um **relatório técnico resumido** para suporte ou diagnóstico especializado. Deseja isso?
