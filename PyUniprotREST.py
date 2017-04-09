import requests
import sys
import urllib2


class PyUniprotREST:
    def __init__(self,type):
        if type == "proteins":
            self.url = 'https://www.ebi.ac.uk/proteins/api/proteins'
        elif type == "features":
            self.url = 'https://www.ebi.ac.uk/proteins/api/features'
        else :
            print "Type not found "
            sys.exit()


    def getbyAccession(self, accession):
        self.accession = accession
        url = self.url + '/' + accession
        try:
            r = requests.get(url, headers={"Accept": "application/json"})
            return r.text
        except:
            r.raise_for_status()
            sys.exit()

    def getbyAccessioninFASTA(self, accession):
        self.accession = accession
        response = urllib2.urlopen('http://www.uniprot.org/uniprot/'+ accession+'.fasta')
        return response.read()




