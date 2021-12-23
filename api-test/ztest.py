# For webhook signing verification, not used just leaving

import hmac
import base64

import pdb

SIGNING_SECRET_SECRET=b'abc123'
#SIGNING_SECRET_SECRET = b'HRkRd4BeOAoUkfZr-mhauJT64rvBASlJRoIyPsd3zeA=' #dont get excited, its from the docs

BODY = '{"start": "2021-07-25T10:00:00", "end": "2021-07-25T11:00:00"}'.encode()
TIMESTAMP = '2021-07-25T10:00:00Z'.encode()
SIGNATURE = 'tRDSF7URY8BLCDlaBcQ7FHu051Zk+aAB0NKMP53teMw='.encode()

def getdigest(secret=SIGNING_SECRET_SECRET, body=BODY, timestamp=TIMESTAMP):
    #pdb.set_trace()
    hm = hmac.new(SIGNING_SECRET_SECRET, digestmod='sha256')
    hm.update(body)
    hm.update(timestamp)
    comp1=base64.b64encode(hm.digest())
    hmac.compare_digest(comp1, SIGNATURE)
    print(f'signature digest = {comp1}')

if __name__ == '__main__':
    getdigest()

