if (sm.getChr().getJob() == 2003):
    sm.lockInGameUI(True)
    sm.playVideoByScript("phantom.avi")
    while sm.getChr().getLevel() != 10:
        sm.addLevel(1)

    sm.setJob(2400)
    sm.setSTR(4)
    sm.setINT(4)
    sm.setDEX(4)
    sm.setLUK(35)
    sm.setAP(23)
    sm.setMaxHP(344)
    sm.setMaxMP(163)
    sm.giveAndEquip(1362001)
    sm.giveAndEquip(1352100)
    sm.giveItem(2000019, 50)
    sm.giveItem(1142375)
    sm.completeQuest(25000)
    sm.lockInGameUI(False)
    sm.dispose()
