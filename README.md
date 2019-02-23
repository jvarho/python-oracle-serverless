python-oracle-serverless
===

Example project for showing how to integrate Oracle's database drivers
with a serverless Python project deployed to AWS Lambda.

Steps to install and deploy:

1. `nvm install`

2. `npm install`

3. Download Oracle Instant Client Basic Lite zip. I.e. the file
    instantclient-basiclite-linux.x64-18.3.0.0.0dbru.zip or a newer version
    from from Oracle:

        https://www.oracle.com/technetwork/topics/linuxx86-64soft-092277.html

4. Extract the files intoto the lib/ folder here.
    (Do not include the instantclient_18_3 folder, only its contents.)

5. Add libaio.so.1 under lib/ – copy from /lib/x86_64-linux-gnu/libaio.so.1 on
    Ubuntu or wherever you can acquire it.

5. `npm run sls-deploy` (requires aws credentials set up)


That should be it.

Obviously you will need to set your database address and credentials
to actually do anything, but you should be able to see whether drivers
load correctly even without them.

If there is a driver problem `npm run sls-logs` will show something like:

DPI-1047: Cannot locate a 64-bit Oracle Client library: "libclntsh.so: cannot
open shared object file: No such file or directory". See
https://oracle.github.io/odpi/doc/installation.html#linux for help:
DatabaseError

OTOH, the following indicates the driver was loaded successfully:

cx_Oracle.DatabaseError: ORA-12154: TNS:could not resolve the connect
identifier specified


Pitfalls:
---

The size of the resulting zip (.serverless/aws-python.zip) contents
is close to the 250 MiB uncompressed size limit of AWS Lambda.

If you get an error like:

An error occurred: HelloLambdaFunction - Unzipped size must be smaller than
262144000 bytes (Service: AWSLambdaInternal; Status Code: 400; Error Code:
InvalidParameterValueException; Request ID: ...).

You may have:

1. Downloaded the wrong driver (basic lite is the smallest).
2. Messed up the symlinks in lib/ – if the files get duplicated it goes over.
3. Added too many dependencies of your own.

In the last case, you may want to try dropping some of the files under lib/
– the .jars at least should be unnecessary.
