import time
from blockchain.neo.switcheo import SwitcheoSmartContract

if __name__ == "__main__":
    rpc_hostname = ''
    rpc_port = ''
    rpc_tls = True
    mongodb_protocol = ''
    mongodb_user = ''
    mongodb_password = ''
    mongodb_hostname = ''
    mongodb_port = ''
    ssc = SwitcheoSmartContract(rpc_hostname=rpc_hostname, rpc_port=rpc_port, rpc_tls=rpc_tls,
                                mongodb_user=mongodb_user, mongodb_password=mongodb_password,
                                mongodb_hostname=mongodb_hostname, mongodb_db=mongodb_db)

    while True:
        print('NEO Block Height: ' + str(ssc.get_neo_block_height()))
        print('NEO Blocks Ingested: ' + str(ssc.ni.mongo_client['neo']['blocks'].count()))
        ssc.ingest_missing_neo_blocks()
        time.sleep(30)
