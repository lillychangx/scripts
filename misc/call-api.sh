#!/bin/bash

echo "hello world"

#curl http://www.centos.org
# client_619293
# {"access_token":"1ff6ff24-f18b-47bf-bc22-62bafec35c2a","token_type":"bearer","expires_in":2591999,"scope":"read write"}\n




#curl https://api.vistara.io/auth/oauth/token -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=client_credentials&client_id=zQVsBhJSSDm7CTB6JNNWTwcPTzeDfDwa&client_secret=B9ENDxb67kzpDx4fGaSz5gHfRYZvJdzDsFuvuESpgEcktDEtmfRfqMGmvcH2m23j"          -X POST

echo "\n"

#curl https://api.vistara.io/api/v2/tenants/client_619293/devices/search  -H "Authorization: Bearer 1ff6ff24-f18b-47bf-bc22-62bafec35c2a" -H "Content-Type: application/json" 



curl https://api.vistara.io/api/v2/tenants/client_619293/devices/934fcbaa-8a8b-4c34-9d24-f3b78ac188cb/deviceWarranty \
-H "Authorization: Bearer 1ff6ff24-f18b-47bf-bc22-62bafec35c2a" \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"purchaseDate": "2015-11-09 12:30:00 UTC", "warrantyExpireDate": "2020-12-09 12:30:00 UTC"}' \
-X POST




