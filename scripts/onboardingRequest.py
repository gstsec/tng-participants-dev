import os
import sys

repo = sys.argv[1]

if repo == "repo":
  with open('temp/verifyResult') as f:
    result = f.readline()   
    if not result:
        raise Exception("Bad verification.")
    else:
        os.system("echo 'Verification was good.'")

with open('temp/country') as f:
  country = f.readline().replace("\n","")

branchName = country+"/onboardingRequest" 
os.system("git checkout -b" + branchName +" > /dev/null 2>&1")
os.system("rm -rf "+ country)
os.system("mkdir " + country)
os.system("mv  -v "+repo+"/onboarding " + country + "/ > /dev/null 2>&1" )
os.system("[ -f "+country + "/onboarding/DCC/auth"+" ] && mv " + country + "/onboarding/DCC/auth "+ country+"/onboarding/DCC/TLS")
os.system("[ -f "+country + "/onboarding/DCC/csca"+" ] && mv " + country + "/onboarding/DCC/csca "+ country+"/onboarding/DCC/SCA")
os.system("[ -f "+country + "/onboarding/DCC/up"+" ] && mv " + country + "/onboarding/DCC/up "+ country+"/onboarding/DCC/UP")
os.system("[ -f "+country + "/onboarding/DCC/CSCA.pem"+" ] && mv " + country + "/onboarding/DCC/SCA/CSCA.pem "+ country+"/onboarding/DCC/SCA/SCA.pem")
os.system("git add "+ country)
os.system("git commit -m 'Bot added Files from "+country+"' > /dev/null 2>&1")
os.system("git push -f -u origin "+ branchName + " > /dev/null 2>&1")
