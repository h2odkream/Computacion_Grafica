#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame

def loadImages():
    images = {}
    #-------------------------------------------------------------------
    images["background"] = pygame.image.load("game_files/background.png").convert()
    images["intro"] = pygame.image.load("game_files/intro.png").convert()
    images["playerFront"] = pygame.image.load("game_files/p3_walk01.png").convert_alpha()
    images["playerWalk01"] = pygame.image.load("game_files/p3_walk01.png").convert_alpha()
    images["playerWalk02"] = pygame.image.load("game_files/p3_walk02.png").convert_alpha()
    images["playerWalk03"] = pygame.image.load("game_files/p3_walk03.png").convert_alpha()
    images["playerJump"] = pygame.image.load("game_files/p3_walk03.png").convert_alpha()
    
    images["grassCliff"] = pygame.image.load("game_files/grassCliff.png").convert_alpha()
    images["grassCliffAlt"] = pygame.image.load("game_files/grassCliffAlt.png").convert_alpha()

    images["grassLeft"] = pygame.image.load("game_files/grassLeft.png").convert_alpha()
    images["grassMid"] = pygame.image.load("game_files/grassMid.png").convert_alpha()
    images["grassRight"] = pygame.image.load("game_files/grassRight.png").convert_alpha()
    images["grassCenter"] = pygame.image.load("game_files/grassCenter.png").convert_alpha()
    images["fence"] = pygame.image.load("game_files/fence.png").convert_alpha()
    images["castle"] = pygame.image.load("game_files/castle.png").convert_alpha()
    images["castleHalf"] = pygame.image.load("game_files/castleHalf.png").convert_alpha()
    images["castleHalfLeft"] = pygame.image.load("game_files/castleHalfLeft.png").convert_alpha()
    images["castlebase"]=pygame.image.load("game_files/castlebase.png")
    images["brickWall"] = pygame.image.load("game_files/brickWall.png").convert_alpha()
    
    images["castleHalfMid"] = pygame.image.load("game_files/castleHalfMid.png").convert_alpha()
    images["castleHalfRight"] = pygame.image.load("game_files/castleHalfRight.png").convert_alpha()
    
    images["castleLeft"] = pygame.image.load("game_files/castleLeft.png").convert_alpha()
    images["castleMid"] = pygame.image.load("game_files/castleMid.png").convert_alpha()
    images["castleRight"] = pygame.image.load("game_files/castleRight.png").convert_alpha()
    
    images["liquidWater"] = pygame.image.load("game_files/liquidWater.png").convert_alpha()
    images["liquidWaterTop_mid"] = pygame.image.load("game_files/liquidWaterTop_mid.png").convert_alpha()
    
    images["grassHalfLeft"] = pygame.image.load("game_files/grassHalfLeft.png").convert_alpha()
    images["grassHalfMid"] = pygame.image.load("game_files/grassHalfMid.png").convert_alpha()
    images["grassHalfRight"] = pygame.image.load("game_files/grassHalfRight.png").convert_alpha()
    
    images["grassHalf"] = pygame.image.load("game_files/grassHalf.png").convert_alpha()
    
    images["boxCoin"] = pygame.image.load("game_files/boxCoin.png").convert_alpha()
    images["boxCoin_disabled"] = pygame.image.load("game_files/boxCoin_disabled.png").convert_alpha()
    images["box2"] = pygame.image.load("game_files/box2.png").convert_alpha()
    images["boxCoinAlt"] = pygame.image.load("game_files/boxCoinAlt.png").convert_alpha()
    images["boxCoinAlt_disabled"] = pygame.image.load("game_files/boxCoinAlt_disabled.png").convert_alpha()
    
    images["slime"] = pygame.image.load("game_files/slimeWalk1.png").convert_alpha()
    images["slime2"] = pygame.image.load("game_files/slimeWalk2.png").convert_alpha()
    images["slimeDead"] = pygame.image.load("game_files/slimeDead.png").convert_alpha()
    
    images["enemigo1"] = pygame.image.load("game_files/enemigo1.png").convert_alpha()
    images["enemigo2"] = pygame.image.load("game_files/enemigo2.png").convert_alpha()
    images["enemigo3"] = pygame.image.load("game_files/enemigo3.png").convert_alpha()
    images["enemigo4"] = pygame.image.load("game_files/enemigo4.png").convert_alpha()

    
    images["hud_0"] = pygame.image.load("game_files/hud_0.png").convert_alpha()
    images["hud_1"] = pygame.image.load("game_files/hud_1.png").convert_alpha()
    images["hud_2"] = pygame.image.load("game_files/hud_2.png").convert_alpha()
    images["hud_3"] = pygame.image.load("game_files/hud_3.png").convert_alpha()
    images["hud_4"] = pygame.image.load("game_files/hud_4.png").convert_alpha()
    images["hud_5"] = pygame.image.load("game_files/hud_5.png").convert_alpha()
    images["hud_6"] = pygame.image.load("game_files/hud_6.png").convert_alpha()
    images["hud_7"] = pygame.image.load("game_files/hud_7.png").convert_alpha()
    images["hud_8"] = pygame.image.load("game_files/hud_8.png").convert_alpha()
    images["hud_9"] = pygame.image.load("game_files/hud_9.png").convert_alpha()
    
    images["hud_p3Alt"] = pygame.image.load("game_files/hud_p3Alt.png").convert_alpha()
    images["hud_x"] = pygame.image.load("game_files/hud_x.png").convert_alpha()
    images["hud_coin"] = pygame.image.load("game_files/hud_coins.png").convert_alpha()
    images["hud_gem_blue"] = pygame.image.load("game_files/hud_gem_blue.png").convert_alpha()
    images["hud_gem_green"] = pygame.image.load("game_files/hud_gem_green.png").convert_alpha()
    images["SpringDown"] = pygame.image.load("game_files/springboardDown.png").convert_alpha()
    images["SpringUp"] = pygame.image.load("game_files/springboardUp.png").convert_alpha()
    images["weight"] = pygame.image.load("game_files/weight.png").convert_alpha()
    images["weightChained"] = pygame.image.load("game_files/weightChained.png").convert_alpha()
    images["chain"] = pygame.image.load("game_files/chain.png").convert_alpha()
    
    images["tochLit"] = pygame.image.load("game_files/tochLit.png").convert_alpha()
    images["tochLit2"] = pygame.image.load("game_files/tochLit2.png").convert_alpha()
    
    images["snailWalk1"] = pygame.image.load("game_files/snailWalk1.png").convert_alpha()
    images["snailWalk2"] = pygame.image.load("game_files/snailWalk2.png").convert_alpha()
    
    images["snailShell"] = pygame.image.load("game_files/snailShell.png").convert_alpha()
    
    images["flagBlue"] = pygame.image.load("game_files/flagBlue.png").convert_alpha()
    images["flagBlue2"] = pygame.image.load("game_files/flagBlue2.png").convert_alpha()
    
    images["flagGreen"] = pygame.image.load("game_files/flagGreen.png").convert_alpha()
    images["flagGreen2"] = pygame.image.load("game_files/flagGreen2.png").convert_alpha()
    
    images["signExit"] = pygame.image.load("game_files/signExit.png").convert_alpha()
    
    images["fly1"] = pygame.image.load("game_files/flyFly1.png").convert_alpha()
    images["fly2"] = pygame.image.load("game_files/flyFly2.png").convert_alpha()
    images["flyDead"] = pygame.image.load("game_files/flyDead.png").convert_alpha()
    
    images["liquidLavaTop_mid"] = pygame.image.load("game_files/liquidLavaTop_mid.png").convert_alpha()
    
    images["sandHalf"] = pygame.image.load("game_files/sandHalf.png").convert_alpha()
    images["sandHalfLeft"] = pygame.image.load("game_files/sandHalfLeft.png").convert_alpha()
    images["sandHalfMid"] = pygame.image.load("game_files/sandHalfMid.png").convert_alpha()
    images["sandHalfRight"] = pygame.image.load("game_files/sandHalfRight.png").convert_alpha()
    
    images["sandLeft"] = pygame.image.load("game_files/sandLeft.png").convert_alpha()
    images["sandMid"] = pygame.image.load("game_files/sandMid.png").convert_alpha()
    images["sandRight"] = pygame.image.load("game_files/sandRight.png").convert_alpha()
    #-------------------------------------------------------------------
    return images
    
def loadSounds():
    sounds = {}
    #-------------------------------------------------------------------
    sounds["coin"] = pygame.mixer.Sound("game_files/coin_sound.ogg")
    sounds["box"] = pygame.mixer.Sound("game_files/box_sound.ogg")
    sounds["spring"] = pygame.mixer.Sound("game_files/spring.ogg")
    sounds["weight"] = pygame.mixer.Sound("game_files/weight_sound.ogg")
    sounds["slime"] = pygame.mixer.Sound("game_files/slime.ogg")
    sounds["jump"] = pygame.mixer.Sound("game_files/Jump17.ogg")
    sounds["waterSplash"] = pygame.mixer.Sound("game_files/watersplash.ogg")
    sounds["coin"] = pygame.mixer.Sound("game_files/coin_sound.ogg")
    sounds["button"] = pygame.mixer.Sound("game_files/button.ogg")
    #-------------------------------------------------------------------
    return sounds
