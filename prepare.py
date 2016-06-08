import zipfile
import sys

xsecfile = sys.argv[1]
templatefile = sys.argv[2]
datasetsfile = sys.argv[3]

print 'xsecfile: {}'.format(xsecfile)
print 'template: {}'.format(templatefile)
print 'datasets: {}'.format(datasetsfile)
print '-'*30

datasets = [x.strip() for x in open(datasetsfile).readlines()]

template = open(templatefile).read()
print template.format(DATASET = 'dataset...', MODEL = '12345')
# sys.exit(0)
for ds in datasets:
    dsid = ds.split('.')[1]
    print 'dsid: {} dataset: {}'.format(dsid,ds)
    print 'add dummy.eff'
    print 'add zara.root'
    print 'add input.yaml'
    zf = zipfile.ZipFile('{}.zip'.format(dsid),'w')
    zf.write('zara.root')
    zf.write('dummy.eff')
    zf.writestr('input.yaml',template.format(DATASET = ds, MODEL = dsid))
    zf.close()