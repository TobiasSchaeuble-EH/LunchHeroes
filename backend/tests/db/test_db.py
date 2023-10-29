from lunchheros.match import matching

test_data = '[{"id":"b994511a-4b7c-4d52-bb26-baeffde1df7d"},{"id":"6ea2070c-18e4-4946-83a4-c41584b3eb9a"},{"id":"f60d3486-e6da-45d9-8a68-b39634c2c1c2"},{"id":"89bce073-f759-4290-87dc-87c63a54c553"},{"id":"456732ea-1a2c-42ed-8d9a-4ff83cc9391d"},{"id":"4404a8a1-3429-45f0-b516-2656cfd96643"},{"id":"08e11522-0d52-4014-9c47-d0b4f27b6716"},{"id":"6923fe00-70dd-4bf6-8c7a-7a15c6f8482e"},{"id":"797ee2cb-5c90-4a09-b15d-f4902193b618"},{"id":"aa3e50f0-091a-458f-a62a-caa586b77751"},{"id":"cfc5a3ec-9fdb-4d8a-b380-4737f7e4c5ed"},{"id":"460c2346-459b-4eaa-b821-b6778be53b14"},{"id":"3738d56c-615c-4129-b389-34b75e788580"},{"id":"d50d37d3-f718-40ea-b3b3-c54593b9b048"},{"id":"5e933bdf-29ca-45fb-8f45-3e4c4805ca60"},{"id":"683bcf3c-f855-4164-9057-a5266fb685e3"},{"id":"85e9d50a-a110-44c7-a512-9c6e285fde09"},{"id":"dd1b225d-4320-4aa2-8873-c25ca5307fbf"},{"id":"5423ae0b-0535-443b-89ab-9defd6ee6eda"},{"id":"ad53c0f5-6a93-4904-bfec-22bf7da98ef4"},{"id":"3dc8e3eb-be7c-4e1f-a92d-7ce3b3ee42c3"},{"id":"691888e2-536e-4183-ae98-1d03e643eeb4"},{"id":"a8e24543-0251-41d7-9eff-dbb3b2690d23"},{"id":"da7762a0-5172-4d6f-ab2f-9eb7a953bd9e"},{"id":"a9a3c0b6-df0a-4b39-b613-582703201145"},{"id":"25d411a2-5ac9-445f-a33f-25ece3dde23b"},{"id":"1784f97e-9f3b-4059-a8b4-7c23c3c8897d"},{"id":"7819f098-6772-4aa8-895e-d193199514c8"},{"id":"1df69d95-dbf5-4e68-a102-01974ea7939c"},{"id":"abb3dead-c9e4-4dbd-922a-c7fbe8f448a8"},{"id":"654a36f8-7b36-4ec1-a02e-e45c3673442e"},{"id":"9edeb3f4-ee7e-417e-aaee-d7a40ed0f24a"},{"id":"3f1cec4e-b1ea-4d0f-91d6-f3ff964b2bf1"},{"id":"ce821535-9969-4a93-9b8d-a80a6242f998"},{"id":"f154a6c9-e1b0-4b67-97ab-d65c69ebed69"},{"id":"04b91fd2-78cf-4779-bd7f-0c0bca1c5187"},{"id":"447e63ba-a69b-4b0a-9bfd-6c9d8b19026a"},{"id":"2229ba43-1c63-425e-b157-1368399b2d73"},{"id":"ae4b46d4-984d-44ed-9e3c-cf8823bb0ebf"},{"id":"c9339894-43fb-45e6-b7ba-f527eeb4a3ea"},{"id":"7c047b21-be3c-427e-92c2-82b7fd7459d3"},{"id":"ee3ed5cf-718d-4d34-bfee-b54057870f7e"},{"id":"787dd532-a1c5-4d15-a371-35e6b5e6a169"},{"id":"9bb0689f-4018-40af-9224-1d2595e75801"},{"id":"bb8bd4e1-dce6-46d9-b9b1-20b46a0bfd68"},{"id":"ae93a1ab-921c-4062-95d9-fcd11357a4b6"},{"id":"4837001a-73b0-4b18-bfda-caccee8aef7f"},{"id":"d007dc20-8bae-4c58-b634-ec42e334e0b6"},{"id":"c6e4f2c4-5ed2-4d8f-9075-36b3f77abc37"},{"id":"dc1b7985-aa01-4087-9b35-f6fa6dc6e2b0"},{"id":"00b1fc3d-8e79-4558-af44-ec8d0a6bb3c2"},{"id":"50c17ac7-5e41-4476-b8ba-f59da66885b1"},{"id":"65980da4-879c-401d-9be0-71209c92c62b"},{"id":"bc74a884-7603-4824-be06-6c82091eb24e"},{"id":"a9670953-5906-4190-848c-5a27cdaa12a3"},{"id":"6a23c795-3a9f-4c81-80f8-92ff3088ae36"},{"id":"d2a3fcef-2518-47cd-b038-5bb16599fca9"},{"id":"c549f2c8-862c-4f0a-9302-7784e8ce6608"},{"id":"c7d6a357-368c-454b-a0ef-fcf2da5442b7"},{"id":"dca40f83-27a2-456e-855e-8f5b5df6744e"},{"id":"c93e381b-81a2-485d-9337-5ccb3d33da4c"},{"id":"6bc16283-2b9d-4196-82f1-dafd05805388"},{"id":"541fa596-b1d1-4da2-bb50-26950006c484"},{"id":"7ce5d11c-c44f-4aaf-878e-2e4d14e68339"},{"id":"e77ee698-bdf4-4e62-9dcf-23b10df1bec1"},{"id":"9507a229-592b-4c87-ae04-52e25d22a6bd"},{"id":"fc4ae092-ef73-4cc3-840b-70e9940d33f1"},{"id":"ae29079c-2bfc-4ce3-a924-339b88c59bbf"},{"id":"6e591ada-490e-4174-9ab9-dc4879632c27"},{"id":"e7467801-c20c-4359-b99f-d5d132e51fc7"},{"id":"edc783c5-531f-4f21-a9cc-574451847065"},{"id":"60a7563a-b5b1-4924-936f-9c8deb78cd9d"},{"id":"1cdbc0a9-eba0-4926-b94b-99164328dba3"},{"id":"81be34d5-e71b-456e-a913-21fece836215"},{"id":"48add589-f329-49e9-a151-fae9d44e08f4"},{"id":"dca5539f-c660-488e-99cf-5f9258c6c84e"},{"id":"78888bef-a3e8-4ee1-a54d-c8bd14d30898"},{"id":"aba32f5e-d5a3-4466-bcf6-77eda1de5214"},{"id":"55251bbf-21c0-4f62-a560-ca12f8235342"},{"id":"790de1d5-df0a-4570-943c-f0089d561bc3"},{"id":"90864c9f-612b-457b-8e42-8afb46f3f922"},{"id":"8915ac2c-c740-42df-8fa1-0c1d132bb92e"},{"id":"f48d9896-c80b-4745-abc3-50acfde0a63c"},{"id":"b1434b1c-1a6c-441d-9812-90bdaee1215f"},{"id":"5596fbd9-f33a-4fb0-b844-e6a979a35ac7"},{"id":"bdcf15c4-b164-49ed-a42e-2d6be5fba168"},{"id":"0a1f949e-5d8e-4080-9936-de0f94e26271"},{"id":"57aa5b15-4c93-49c7-8e4c-5c0982353749"},{"id":"8d98509f-464a-4c26-9142-f5903c260a51"},{"id":"5fce6888-9570-4f7b-90c5-be2e9f3f7035"},{"id":"e6940d4a-a287-4dc9-b293-60cabc3b4655"},{"id":"666137b1-ffa8-4612-8e99-08e93691e33b"},{"id":"180d1e45-d8ab-4679-a260-037416c8b9ea"},{"id":"7d11ea4e-f72d-4bf5-a71f-57b373435fd1"},{"id":"81940ce9-34c7-4288-b343-99ea4464493c"},{"id":"3fb80679-0120-4383-8047-e3e8da12d69d"},{"id":"e30ffdaf-2467-42ce-a703-034a478b0417"},{"id":"06cbb2ea-96e0-4896-a425-b098957af37a"},{"id":"cb7e5907-68e7-44bd-95c0-06ccebc075db"},{"id":"bbbbaf3c-1d57-4e11-bf88-9bf92d374b97"},{"id":"bf7c7244-ff86-470c-ba95-07f1e21c9682"},{"id":"4117890c-bdd9-487c-9921-d7a5c9d9b08d"},{"id":"5925b106-1578-45a9-bb30-7fafb37cccdb"},{"id":"00d4050b-614b-4be8-aa16-cab95f6e7dca"},{"id":"4938a261-8083-44d2-955f-c00856f8eb6d"},{"id":"798bdf20-1614-4026-9235-ab10ba228dae"},{"id":"b932c46d-3db7-4cd9-8007-6db3cf2b923b"},{"id":"2e9db169-2094-417e-a775-c8a75790c458"},{"id":"fb16e78e-5ccb-4635-b355-a01f0834389c"},{"id":"9a7ae5aa-b788-49fd-8894-9f899f2a2587"},{"id":"3c3a5aca-6c0e-4e9d-90cb-557fef1256c1"},{"id":"31d574de-869d-4098-be2b-addbfdacebcb"},{"id":"bbaa570b-295b-4bbd-bfd4-02e0b754419e"},{"id":"1e7d409b-03e0-46ef-bdc3-cb55807c10a4"},{"id":"46da386a-c562-4eea-9ae9-c6f87700dbc3"},{"id":"5c5ac49c-a9e9-4fbb-84d1-c5e956f30781"},{"id":"7ddd95e3-3a77-4b61-9d0a-3ffaa1c5a95a"},{"id":"36ad540a-b857-433a-8d07-4087e4d0fe4a"},{"id":"ea88696e-7e9b-49e9-8d65-ace6084425d7"},{"id":"05f6a875-9cc5-4185-8352-0afab880ff4d"},{"id":"6fdb38c9-be3c-44df-9a7a-3f73413842b3"},{"id":"f3313ebc-7b1d-4691-9e65-5ff4e549210a"},{"id":"92cdf84d-485b-4bc6-af29-e9853d20ff5d"},{"id":"878fd4ae-c15c-4325-90f5-4674d04c5455"},{"id":"36e6896d-1814-4348-94f8-a83282d1503b"},{"id":"d6fdf1c7-1333-4382-bac9-4a8a37608b02"},{"id":"37c19c16-e97c-4276-8bf9-97ef7c29d747"}]'

test_data6 = '[{"id":"b994511a-4b7c-4d52-bb26-baeffde1df7d"},{"id":"6ea2070c-18e4-4946-83a4-c41584b3eb9a"},{"id":"f60d3486-e6da-45d9-8a68-b39634c2c1c2"},{"id":"89bce073-f759-4290-87dc-87c63a54c553"},{"id":"456732ea-1a2c-42ed-8d9a-4ff83cc9391d"},{"id":"4404a8a1-3429-45f0-b516-2656cfd96643"}]'

test_data3 = '[{"id":"b994511a-4b7c-4d52-bb26-baeffde1df7d"},{"id":"6ea2070c-18e4-4946-83a4-c41584b3eb9a"},{"id":"f60d3486-e6da-45d9-8a68-b39634c2c1c2"}]'

test_data2 = '[{"id":"b994511a-4b7c-4d52-bb26-baeffde1df7d"},{"id":"6ea2070c-18e4-4946-83a4-c41584b3eb9a"}]'

test_data4 = '[{"id":"b994511a-4b7c-4d52-bb26-baeffde1df7d"},{"id":"6ea2070c-18e4-4946-83a4-c41584b3eb9a"},{"id":"f60d3486-e6da-45d9-8a68-b39634c2c1c2"},{"id":"89bce073-f759-4290-87dc-87c63a54c553"}]'

test_data7 = '[{"id":"b994511a-4b7c-4d52-bb26-baeffde1df7d"},{"id":"6ea2070c-18e4-4946-83a4-c41584b3eb9a"},{"id":"f60d3486-e6da-45d9-8a68-b39634c2c1c2"},{"id":"89bce073-f759-4290-87dc-87c63a54c553"},{"id":"456732ea-1a2c-42ed-8d9a-4ff83cc9391d"},{"id":"4404a8a1-3429-45f0-b516-2656cfd96643"},{"id":"08e11522-0d52-4014-9c47-d0b4f27b6716"}]'

test_data8 = '[{"id":"b994511a-4b7c-4d52-bb26-baeffde1df7d"},{"id":"6ea2070c-18e4-4946-83a4-c41584b3eb9a"},{"id":"f60d3486-e6da-45d9-8a68-b39634c2c1c2"},{"id":"89bce073-f759-4290-87dc-87c63a54c553"},{"id":"456732ea-1a2c-42ed-8d9a-4ff83cc9391d"},{"id":"4404a8a1-3429-45f0-b516-2656cfd96643"},{"id":"08e11522-0d52-4014-9c47-d0b4f27b6716"}]'

test_data8 = '[{"id":"b994511a-4b7c-4d52-bb26-baeffde1df7d"},{"id":"6ea2070c-18e4-4946-83a4-c41584b3eb9a"},{"id":"f60d3486-e6da-45d9-8a68-b39634c2c1c2"},{"id":"89bce073-f759-4290-87dc-87c63a54c553"},{"id":"456732ea-1a2c-42ed-8d9a-4ff83cc9391d"},{"id":"4404a8a1-3429-45f0-b516-2656cfd96643"},{"id":"08e11522-0d52-4014-9c47-d0b4f27b6716"},{"id":"6923fe00-70dd-4bf6-8c7a-7a15c6f8482e"}]'
test_data9 = '[{"id":"b994511a-4b7c-4d52-bb26-baeffde1df7d"},{"id":"6ea2070c-18e4-4946-83a4-c41584b3eb9a"},{"id":"f60d3486-e6da-45d9-8a68-b39634c2c1c2"},{"id":"89bce073-f759-4290-87dc-87c63a54c553"},{"id":"456732ea-1a2c-42ed-8d9a-4ff83cc9391d"},{"id":"4404a8a1-3429-45f0-b516-2656cfd96643"},{"id":"08e11522-0d52-4014-9c47-d0b4f27b6716"},{"id":"6923fe00-70dd-4bf6-8c7a-7a15c6f8482e"},{"id":"797ee2cb-5c90-4a09-b15d-f4902193b618"}]'

test_data10 = '[{"id":"b994511a-4b7c-4d52-bb26-baeffde1df7d"},{"id":"6ea2070c-18e4-4946-83a4-c41584b3eb9a"},{"id":"f60d3486-e6da-45d9-8a68-b39634c2c1c2"},{"id":"89bce073-f759-4290-87dc-87c63a54c553"},{"id":"456732ea-1a2c-42ed-8d9a-4ff83cc9391d"},{"id":"4404a8a1-3429-45f0-b516-2656cfd96643"},{"id":"08e11522-0d52-4014-9c47-d0b4f27b6716"},{"id":"6923fe00-70dd-4bf6-8c7a-7a15c6f8482e"},{"id":"797ee2cb-5c90-4a09-b15d-f4902193b618"},{"id":"aa3e50f0-091a-458f-a62a-caa586b77751"}]'

test_data11 = '[{"id":"b994511a-4b7c-4d52-bb26-baeffde1df7d"},{"id":"6ea2070c-18e4-4946-83a4-c41584b3eb9a"},{"id":"f60d3486-e6da-45d9-8a68-b39634c2c1c2"},{"id":"89bce073-f759-4290-87dc-87c63a54c553"},{"id":"456732ea-1a2c-42ed-8d9a-4ff83cc9391d"},{"id":"4404a8a1-3429-45f0-b516-2656cfd96643"},{"id":"08e11522-0d52-4014-9c47-d0b4f27b6716"},{"id":"6923fe00-70dd-4bf6-8c7a-7a15c6f8482e"},{"id":"797ee2cb-5c90-4a09-b15d-f4902193b618"},{"id":"aa3e50f0-091a-458f-a62a-caa586b77751"},{"id":"cfc5a3ec-9fdb-4d8a-b380-4737f7e4c5ed"}]'

def test_matching():

    grouping = matching(test_data)

    print(grouping)
    return grouping

def test_matching2():

    grouping = matching(test_data2)

    print(grouping)

    # assert if we get one group of 6 people
    # the first group should have 6 people
    assert len(grouping[0]) == 2

    return grouping


def test_matching4():

    grouping = matching(test_data4)

    print(grouping)

    # assert if we get one group of 6 people
    # the first group should have 6 people
    assert len(grouping[0]) == 4

    return grouping

def test_matching3():

    grouping = matching(test_data3)

    print(grouping)

    # assert if we get one group of 6 people
    # the first group should have 6 people
    assert len(grouping[0]) == 3

    return grouping


def test_matching6():

    grouping = matching(test_data6)

    print(grouping)

    # assert if we get one group of 6 people
    # the first group should have 6 people
    assert len(grouping[0]) == 6

    return grouping


def test_matching7():

    grouping = matching(test_data7)

    print(grouping)

    # assert if we get one group of seven people
    # the first group should have 7 people
    assert len(grouping[0]) == 7

    return grouping




def test_matching8():

    grouping = matching(test_data8)

    print(grouping)
    # assert if we get two groups of 4 people
    # the first group should have 4 people
    assert len(grouping[0]) == 4
    # the second group should have 4 people
    assert len(grouping[1]) == 4

    return grouping


def test_matching9():

    grouping = matching(test_data9)

    print(grouping)

    # assert if we get two groups of 4 people
    # the first group should have 5 people
    assert len(grouping[0]) == 5
    # the second group should have 4 people
    assert len(grouping[1]) == 4

    return grouping

def test_matching10():

    grouping = matching(test_data10)

    print(grouping)

    # assert if we get two groups of 4 people
    # the first group should have 5 people
    assert len(grouping[0]) == 5
    # the second group should have 5 people
    assert len(grouping[1]) == 5

    return grouping

def test_matching11():

    grouping = matching(test_data11)

    print(grouping)

    # assert if we get two groups of 4 people
    # the first group should have 6 people
    assert len(grouping[0]) == 6
    # the second group should have 5 people
    assert len(grouping[1]) == 5


    return grouping