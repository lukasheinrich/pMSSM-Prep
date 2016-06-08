import ROOT
import array
import sys

def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    f = ROOT.TFile(output_file,'recreate')
    tree = ROOT.TTree('SignalUncertainties','SignalUncertainties')
    
    a = array.array('d',[2])

    names  = ['modelName','finalState','crossSection','Tot_error']
    spec   = ['modelName/I','finalState/I','crossSection/D','Tot_error/D']
    tc     = ['i','i','d','d']
    arrs   = []
    for i,(n,s,t) in enumerate(zip(names,spec,tc)):
        arrs += [array.array(t,[0])]
        getattr(tree,'Branch')(n,arrs[i],s)
    
    
    with open(input_file) as inputfile:
        for line in inputfile.readlines():
            types = [int,int,float,float,float,float]
            data = dsid, fs, xsec, filtereff, br, uncrt = [t(v) for t,v in zip(types,line.split())]
            arrs[0][0] = dsid
            arrs[1][0] = fs
            arrs[2][0] = xsec*filtereff*br
            arrs[3][0] = uncrt
            tree.Fill()
    tree.Write()
    f.Close()

    single_effs = {}
    allfs = []
    with open(input_file) as inputfile:
        for line in inputfile.readlines():
            types = [int,int,float,float,float,float]
            data = dsid, fs, xsec, filtereff, br, uncrt = [t(v) for t,v in zip(types,line.split())]
            allfs += [fs]

    uniq_fs = set(allfs)
    with open('dummy.eff','w') as f:
        f.write('ch,eff\n')
        for fs in uniq_fs:
            f.write('{fs},1.00\n'.format(fs = fs))
            
if __name__ == '__main__':
    
    main()