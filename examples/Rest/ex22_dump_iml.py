# Copyright 2016 Hewlett Packard Enterprise Development LP
 #
 # Licensed under the Apache License, Version 2.0 (the "License"); you may
 # not use this file except in compliance with the License. You may obtain
 # a copy of the License at
 #
 #      http://www.apache.org/licenses/LICENSE-2.0
 #
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 # WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 # License for the specific language governing permissions and limitations
 # under the License.

import sys
from restobject import RestObject

def ex22_dump_iml(restobj):
    sys.stdout.write("\nEXAMPLE 22: Dump Integrated Management Log\n")
    instances = restobj.search_for_type("LogService.")

    for instance in instances:
        if instance["href"].endswith("IML"):
            tmp = restobj.rest_get(instance["href"])

            for entry in tmp.dict["links"]["Entries"]:
                response = restobj.rest_get(entry["href"])
                
                for log_entry in response.dict["Items"]:
                    sys.stdout.write(log_entry["Severity"] + ": Class " + \
                         str(log_entry["Oem"]["Hp"]["Class"]) + \
                         " / Code " + str(log_entry["Oem"]["Hp"]["Code"]) + \
                         ":\t" + log_entry["Message"] + "\n")

if __name__ == "__main__":
    # When running on the server locally use the following commented values
    # iLO_host = "blobstore://."
    # iLO_account = "None"
    # iLO_password = "None"

    # When running remotely connect using the iLO address, iLO account name, 
    # and password to send https requests
    iLO_host = "https://16.83.63.43"
    iLO_account = "admin"
    iLO_password = "password"
    
    #Create a REST object
    REST_OBJ = RestObject(iLO_host, iLO_account, iLO_password)
    ex22_dump_iml(REST_OBJ)
