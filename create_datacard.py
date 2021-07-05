import ROOT
from ROOT import TFile, TTree, TCanvas, TGraph, TMultiGraph, TGraphErrors, TLegend
#import CMS_lumi, tdrstyle
#import subprocess # to execute shell command
ROOT.gROOT.SetBatch(ROOT.kTRUE)
import sys

print("Enter masspoint signal DPS_VV EWK_VV VV WJets DYJets Higgs QCD VVV ttX EWK_V SingleTop Vgamma tt in order")
def print_sampleinfo():
    mass_value = sys.argv[1]
    file1 = open(sys.argv[2],"r+")
    file2 = open(sys.argv[3],"r+")
    file3 = open(sys.argv[4],"r+")
    file4 = open(sys.argv[5],"r+")
    file5 = open(sys.argv[6],"r+")
    file6 = open(sys.argv[7],"r+")
    file7 = open(sys.argv[8],"r+")
    file8 = open(sys.argv[9],"r+")
    file9 = open(sys.argv[10],"r+")
    file10 = open(sys.argv[11],"r+")
    file11 = open(sys.argv[12],"r+")
    file12 = open(sys.argv[13],"r+")
    file13 = open(sys.argv[14],"r+")
    file14 = open(sys.argv[15],"r+")


if (len(sys.argv) < 10):
       print("Please enter inputs in order")
       sys.exit()

for i in range(len(sys.argv)):
    print(sys.argv[i])

mass_value = sys.argv[1]
file1 = open(sys.argv[2],"r+")
file2 = open(sys.argv[3],"r+")
file3 = open(sys.argv[4],"r+")
file4 = open(sys.argv[5],"r+")
file5 = open(sys.argv[6],"r+")
file6 = open(sys.argv[7],"r+")
file7 = open(sys.argv[8],"r+")
file8 = open(sys.argv[9],"r+")
file9 = open(sys.argv[10],"r+")
file10 = open(sys.argv[11],"r+")
file11 = open(sys.argv[12],"r+")
file12 = open(sys.argv[13],"r+")
file13 = open(sys.argv[14],"r+")
file14 = open(sys.argv[15],"r+")



#signal
lines=file1.readlines()
result=[]
integral=[]
for x in lines:
    integral.append(x.split(' ')[1])
    result.append(x.split(' ')[0])
file1.close()

#bkg1
lines_bkg1=file2.readlines()
result_bkg1=[]
integral_bkg1=[]
for x_bkg1 in lines_bkg1:
    integral_bkg1.append(x_bkg1.split(' ')[1])
    result_bkg1.append(x_bkg1.split(' ')[0])
file2.close()

#bkg2
lines_bkg2=file3.readlines()
result_bkg2=[]
integral_bkg2=[]
for x_bkg2 in lines_bkg2:
    integral_bkg2.append(x_bkg2.split(' ')[1])
    result_bkg2.append(x_bkg2.split(' ')[0])
  #  print(result_bkg2)
file3.close()

#bkg3
lines_bkg3=file4.readlines()
result_bkg3=[]
integral_bkg3=[]
for x_bkg3 in lines_bkg3:
    integral_bkg3.append(x_bkg3.split(' ')[1])
    result_bkg3.append(x_bkg3.split(' ')[0])
file4.close()

#bkg4
lines_bkg4=file5.readlines()
result_bkg4=[]
integral_bkg4=[]
for x_bkg4 in lines_bkg4:
    integral_bkg4.append(x_bkg4.split(' ')[1])
    result_bkg4.append(x_bkg4.split(' ')[0])
file5.close()

#bkg5
lines_bkg5=file6.readlines()
result_bkg5=[]
integral_bkg5=[]
for x_bkg5 in lines_bkg5:
    integral_bkg5.append(x_bkg5.split(' ')[1])
    result_bkg5.append(x_bkg5.split(' ')[0])
file6.close()


#bkg6
lines_bkg6=file7.readlines()
result_bkg6=[]
integral_bkg6=[]
for x_bkg6 in lines_bkg6:
    integral_bkg6.append(x_bkg6.split(' ')[1])
    result_bkg6.append(x_bkg6.split(' ')[0])
file7.close()

#bkg7
lines_bkg7=file8.readlines()
result_bkg7=[]
integral_bkg7=[]
for x_bkg7 in lines_bkg7:
    integral_bkg7.append(x_bkg7.split(' ')[1])
    result_bkg7.append(x_bkg7.split(' ')[0])
file8.close()

#bkg8
lines_bkg8=file9.readlines()
result_bkg8=[]
integral_bkg8=[]
for x_bkg8 in lines_bkg8:
    integral_bkg8.append(x_bkg8.split(' ')[1])
    result_bkg8.append(x_bkg8.split(' ')[0])
file9.close()

#bkg9
lines_bkg9=file10.readlines()
result_bkg9=[]
integral_bkg9=[]
for x_bkg9 in lines_bkg9:
    integral_bkg9.append(x_bkg9.split(' ')[1])
    result_bkg9.append(x_bkg9.split(' ')[0])
file10.close()

#bkg10
lines_bkg10=file11.readlines()
result_bkg10=[]
integral_bkg10=[]
for x_bkg10 in lines_bkg10:
    integral_bkg10.append(x_bkg10.split(' ')[1])
    result_bkg10.append(x_bkg10.split(' ')[0])
file11.close()

#bkg11
lines_bkg11=file12.readlines()
result_bkg11=[]
integral_bkg11=[]
for x_bkg11 in lines_bkg11:
    integral_bkg11.append(x_bkg11.split(' ')[1])
    result_bkg11.append(x_bkg11.split(' ')[0])
file12.close()

#bkg12
lines_bkg12=file13.readlines()
result_bkg12=[]
integral_bkg12=[]
for x_bkg12 in lines_bkg12:
    integral_bkg12.append(x_bkg12.split(' ')[1])
    result_bkg12.append(x_bkg12.split(' ')[0])
file13.close()

#bkg13
lines_bkg13=file14.readlines()
result_bkg13=[]
integral_bkg13=[]
for x_bkg13 in lines_bkg13:
    integral_bkg13.append(x_bkg13.split(' ')[1])
    result_bkg13.append(x_bkg13.split(' ')[0])
file14.close()


#fake systematics
#lines_sys1=file7.readlines()
#result_sys1=[]
#integral_sys1=[]
#for x_sys1 in lines_sys1:
#    integral_sys1.append(x_sys1.split(' ')[0])
#N_sys = len(integral_sys1)
#for i in range(N_sys):
#    number = format(float(integral_sys1[i]),".3f")
#    if float(number) < 1.:
#        name = "/1.000"
#        out = str(number).rstrip()  + name + "\n"
#        #print(out)
#    if float(number) > 1.:
#        name = "1.000/"
#        out = name + str(number).rstrip() + "\n"
#        #print(out)
#    result_sys1.append(out)
##print(len(result_sys1))
#file7.close()

N = len(result)
def createCard(result):
    datacard_lines1 = ["#========= VBF temp",
                   
                    "imax 1  number of channels",
                    "jmax 13  number of backgrounds",
                    "kmax * number of nuisance parameters (sources of systematic uncertainties)",

                    "# we have just one channel and will use some dummy data",
                    "bin vbf_mu",
                    "observation 0",

                    "bin				vbf_mu		vbf_mu		vbf_mu		vbf_mu		vbf_mu		vbf_mu		vbf_mu		vbf_mu		vbf_mu		vbf_mu		vbf_mu		vbf_mu		vbf_mu		vbf_mu		",
                    "process				SIG		DPS_VV		EWK_VV		VV		WJets		DYJets		Higgs		QCD		VVV		ttX		EWK_V		SingleTop	Vgamma		tt		",
                    "process				0		1		2		3		4		5		6		7		8		9		10		11		12		13		",
                    ]
    datacard_sys = ["lumi		lnN		1.025		1.025		1.025		1.025		1.025		1.025		1.025		1.025		1.025		1.025		1.025		1.025		1.025		1.025		",
                "scale		lnN		1.004		-		-		-		-		-		-		-		-		-		-		-		-		-		",
                "pdf   		lnN		1.021		-		-		-		-		-		-		-		-		-		-		-		-		-		",
                "Trig00		lnN		1.03		-		-		-		-		-		-		-		-		-		-		-		-		-		",
                "ttxs		lnN		-		-		-		-		-		-		-		-		-		-		-		-		-		-		",
                "vvxs		lnN		-		-		-		-		-		-		-		-		-		-		-		-		-		-		",
                "stx		lnN		-		-		-		-		-		-		-		-		-		-		-		-		-		-		",
                "dyxs		lnN		-		-		-		-		-		-		-		-		-		-		-		-		-		-		", 
                "MUID		lnN		1.02		-		-		-		-		-		-		-		-		-		-		-		-		-		",
                "ELID		lnN		1.02		-		-		-		-		-		-		-		-		-		-		-		-		-		",
                "TAUID		lnN		1.04		-		-		-		-		-		-		-		-		-		-		-		-		-		",
                "MMS		lnN		1.02		-		-		-		-		-		-		-		-		-		-		-		-		-		",
                "EES		lnN		1.02		-		-		-		-		-		-		-		-		-		-		-		-		-		",
                "BTAG		lnN		-		-		-		-		-		-		-		-		-		-		-		-		-		-		",
                "JER		lnN		1.10		-		-		-		-		-		-		-		-		-		-		-		-		-		",
                "JER		lnN		1.10		-		-		-		-		-		-		-		-		-		-		-		-		-		",
		"ISR		lnN		-		-		-		-		-		-		-		-		-		-		-		-		-		-		",
               ] 
    for i in range(N):
        datacard = open("VBF_card_M"+str(mass_value)+"_bin"+result[i]+".txt",'w')
        input_signal = float(integral[i])
        input_bkg1 =  float(integral_bkg1[i])
        input_bkg2 =  float(integral_bkg2[i])
	input_bkg3 =  float(integral_bkg3[i])
	input_bkg4 =  float(integral_bkg4[i])
	input_bkg5 =  float(integral_bkg5[i])
        input_bkg6 =  float(integral_bkg6[i])
        input_bkg7 =  float(integral_bkg7[i])
        input_bkg8 =  float(integral_bkg8[i])
        input_bkg9 =  float(integral_bkg9[i])
        input_bkg10 =  float(integral_bkg10[i])
        input_bkg11 =  float(integral_bkg11[i])
        input_bkg12 =  float(integral_bkg12[i])
        input_bkg13 =  float(integral_bkg13[i])

#	input_sys1 =  result_sys1[i]
	#print(len(result_sys1))        
	second = result[i]
	
	for line in datacard_lines1:
            datacard.write(line+"\n")
        datacard.write("rate		{:<15.10f} {:<15.10f} {:<15.10f} {:<15.10f} {:<15.10f} {:<15.10f} {:<15.10f} {:<15.10f} {:<15.10f} {:<15.10f} {:<15.10f} {:<15.10f} {:<15.10f} {:<15.10f} \n".format(input_signal, input_bkg1, input_bkg2, input_bkg3, input_bkg4, input_bkg5, input_bkg6, input_bkg7, input_bkg8, input_bkg9, input_bkg10, input_bkg11, input_bkg12, input_bkg13))
        datacard.write("\n")
        for line_sys in datacard_sys:
            datacard.write(line_sys+"\n")
#        datacard.write("wfake   {:<6.10s} {:<14.10s} {:<14.10s} {:<14.10s} {:<14.10s} {:<14.10s} {:<14.10s} \n".format('lnN','-',input_sys1, '-','-','-','-'))

        datacard.close()

def main():
	print_sampleinfo()
	createCard(result)
if __name__ == '__main__':
    main()






