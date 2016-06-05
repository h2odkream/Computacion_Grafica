#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from resources import *
from level_class import Level
#--Images Files:
images = None
#=======================================================================
class Level_One(Level):#Level_One hereda todo los atributos de la clase Level
    limit = (-2000,-500)#tupla de dos elementos
    background_color = (110,191,230)
    music_filename = "game_files/Billie Jean.mp3"
    def __init__(self,imagesFiles,soundsFiles,player):
        Level.__init__(self,imagesFiles,soundsFiles,player)
        #========================
        global images
        images = imagesFiles
        #========================
        for i in range(0,70*8,70):
            platform = Block((i,430),images["grassMid"])
            self.platform_list.add(platform)
        i += 70 
        platform = Block((i,430),images["grassRight"])
        self.platform_list.add(platform)
        
        platform = Platform((280,290),images["grassLeft"])
        self.platform_list.add(platform)
        platform = Platform((350,290),images["grassMid"])
        self.platform_list.add(platform)
        platform = Platform((420,290),images["grassRight"])
        self.platform_list.add(platform)
        
        platform = Platform((140,220),images["grassHalf"])
        self.platform_list.add(platform)
        
        platform = Platform((350,70),images["grassHalfLeft"])
        self.platform_list.add(platform)
        for i in range(420,980,70):
            platform = Platform((i,70),images["grassHalfMid"])
            self.platform_list.add(platform)
        platform = Platform((980,70),images["grassHalfRight"])
        self.platform_list.add(platform)
        
        platform = Platform((140,-70),images["grassCliff"])
        self.platform_list.add(platform)
        
        platform = Platform((2170,0),images["grassCliffAlt"])
        self.platform_list.add(platform)
        
        
        platform = Block((980,430),images["grassLeft"])
        self.platform_list.add(platform)
        for i in range(1050,2730,70):
            platform = Block((i,430),images["grassMid"])
            self.platform_list.add(platform)

            
        platform = Platform((1260,-70),images["grassHalfLeft"])
        self.platform_list.add(platform)
        for i in range(1330,1680,70):
            platform = Platform((i,-70),images["grassHalfMid"])
            self.platform_list.add(platform)
            
        platform = Platform((1680,-70),images["grassHalfRight"])
        self.platform_list.add(platform)
        
        movingPlatform = MovingPlatform((630,350),images["grassHalf"])
        movingPlatform.leftLimit = 630
        movingPlatform.rightLimit = 910
        movingPlatform.changeX = 2
        movingPlatform.level = self
        movingPlatform.player = player
        self.platform_list.add(movingPlatform)
        
        movingPlatform = MovingPlatform((1130,210),images["grassHalf"])
        movingPlatform.bottomLimit = 280
        movingPlatform.topLimit = -140
        movingPlatform.changeY = 2
        movingPlatform.level = self
        movingPlatform.player = player
        self.platform_list.add(movingPlatform)
    
        
        wall = Block((2170,360),images["brickWall"])
        self.block_list.add(wall)
        wall = Block((2170,290),images["brickWall"])
        self.block_list.add(wall)

        hud = Block((70,50),images["hud_coin"])
        self.hud_list.add(hud)
        hud = Block((770,190),images["hud_coin"])
        self.hud_list.add(hud)
        hud = Block((1610,70),images["hud_coin"])
        self.hud_list.add(hud)
        
        hud = Block((190,-140),images["hud_coin"])
        self.hud_list.add(hud)
        hud = Block((260,-140),images["hud_coin"])
        self.hud_list.add(hud)
        
        for i in range(560,980,70):
            hud = Block((i,-20),images["hud_coin"])
            self.hud_list.add(hud)
    
        block = MovableBlock((1260,210),images["boxCoin"],images["boxCoin_disabled"],player)
        block.level = self
        self.block_list.add(block)
        
        slime = AnimatedBlock((1190,430),images["slime"])
        slime.image1 = images["slime"]
        slime.image2 = images["slime2"]
        slime.leftLimit = 980
        slime.rightLimit = 1330
        slime.changeX = -2
        slime.level = self
        slime.player = player
        slime.dead_image = images["slimeDead"]
        self.block_list.add(slime)
        
        slime = AnimatedBlock((1330,-70),images["slime"])
        slime.image1 = images["slime"]
        slime.image2 = images["slime2"]
        slime.leftLimit = 1260
        slime.rightLimit = 1680
        slime.changeX = -2
        slime.level = self
        slime.player = player
        slime.dead_image = images["slimeDead"]
        self.block_list.add(slime)
        
        snail = AnimatedBlock((350,70),images["snailWalk1"])
        snail.image1 = images["snailWalk1"]
        snail.image2 = images["snailWalk2"]
        snail.leftLimit = 350
        snail.rightLimit = 980
        snail.changeX = -2
        snail.level = self
        snail.player = player
        snail.is_snail = True
        snail.dead_image = images["snailShell"]
        self.block_list.add(snail)
        
        enemi_N1 = AnimatedBlock((1750,430),images["enemigo1"])
        enemi_N1.image1 = images["enemigo1"]
        enemi_N1.image2 = images["enemigo2"]
        enemi_N1.leftLimit = 1500
        enemi_N1.rightLimit = 2100
        enemi_N1.changeX = -2
        enemi_N1.level = self
        enemi_N1.player = player
        enemi_N1.dead_image = images["enemigo4"]
        self.block_list.add(enemi_N1)
        
        weight = Weight((1400,210),images["weightChained"],player,self.platform_list,self.items_list)
        self.block_list.add(weight)
        
        fly = Fly((630,210),images["fly1"],images["fly2"])
        self.block_list.add(fly)
        
        exit_sign = Block((2590,360),images["signExit"])
        self.items_list.add(exit_sign)
        
        spring = Spring((140,220),images["SpringDown"],player)
        self.block_list.add(spring)
        
        spring = Spring((2380,430),images["SpringDown"],player)
        self.block_list.add(spring)
        
            
        for i in range(1050,1330,58):
            item = Block((i,360),images["fence"])
            self.items_list.add(item)
            
#========================================================================================

class Level_Two(Level_One):

    background_color = (40,30,50)
    music_filename = "game_files/Thriller_level2.mp3"#Mushroom Theme_0.ogg"
    def __init__(self,imagesFiles,soundsFiles,player):
        Level.__init__(self,imagesFiles,soundsFiles,player)
        #========================
        global images
        images = imagesFiles
        #========================
        for i in range(0,70*5,70):
            platform = Block((i,430),images["castleMid"])
            self.platform_list.add(platform)
        i += 70 
        platform = Block((i,430),images["castleRight"])
        self.platform_list.add(platform)
        
        platform = Block((1190,430),images["castleLeft"])
        self.platform_list.add(platform)
        for i in range(1260,2730,70):
            platform = Block((i,430),images["castleMid"])
            self.platform_list.add(platform)
        i += 70 
        platform = Block((i,430),images["castleRight"])
        self.platform_list.add(platform)
        
        for i in range(0,70*4,70):
            platform = Platform((i,70),images["castleHalfMid"])
            self.platform_list.add(platform)
        i += 70 
        platform = Platform((i,70),images["castleHalfRight"])
        self.platform_list.add(platform)
        
        lava = AnimatedItem((420,430),images["liquidLavaTop_mid"],
                                pygame.transform.flip(images["liquidLavaTop_mid"],True,False))
        self.items_list.add(lava)
        lava = AnimatedItem((490,430),images["liquidLavaTop_mid"],
                                pygame.transform.flip(images["liquidLavaTop_mid"],True,False))
        self.items_list.add(lava)
        
        platform = Block((560,430),images["castleLeft"])
        self.platform_list.add(platform)
        platform = Block((630,430),images["castleMid"])
        self.platform_list.add(platform)
        platform = Block((700,430),images["castleRight"])
        self.platform_list.add(platform)
        
        platform = Platform((770,70),images["castleHalfLeft"])
        self.platform_list.add(platform)
        platform = Platform((840,70),images["castleHalfMid"])
        self.platform_list.add(platform)
        platform = Platform((910,70),images["castleHalfMid"])
        self.platform_list.add(platform)
        platform = Platform((980,70),images["castleHalfRight"])
        self.platform_list.add(platform)
        
        for i in range(770,1190,70):
            lava = AnimatedItem((i,430),images["liquidLavaTop_mid"],
                                pygame.transform.flip(images["liquidLavaTop_mid"],True,False))
            self.items_list.add(lava)
            
        platform = Platform((280,290),images["castleHalf"])
        self.platform_list.add(platform)
        
        platform = Platform((420,220),images["castleHalf"])
        self.platform_list.add(platform)
        
        platform = Platform((560,70),images["castleHalf"])
        self.platform_list.add(platform)

        for i in range(70,280,70):
            hud = Block((i,-70),images["hud_coin"])
            self.hud_list.add(hud)
        
        hud = Block((560,-70),images["hud_coin"])
        self.hud_list.add(hud)
        
        hud = Block((420,0),images["hud_coin"])
        self.hud_list.add(hud)
            
        movingPlatform = MovingPlatform((840,280),images["castleHalf"])
        movingPlatform.leftLimit = 770
        movingPlatform.rightLimit = 1120
        movingPlatform.changeX = 2
        movingPlatform.level = self
        movingPlatform.player = player
        self.platform_list.add(movingPlatform)
        
        snail = AnimatedBlock((1260,430),images["snailWalk1"])
        snail.image1 = images["snailWalk1"]
        snail.image2 = images["snailWalk2"]
        snail.leftLimit = 1190
        snail.rightLimit = 1540
        snail.changeX = -2
        snail.level = self
        snail.player = player
        snail.is_snail = True
        snail.dead_image = images["snailShell"]
        self.block_list.add(snail)
        
        slime = AnimatedBlock((630,430),images["slime"])
        slime.image1 = images["slime"]
        slime.image2 = images["slime2"]
        slime.leftLimit = 560
        slime.rightLimit = 700
        slime.changeX = -2
        slime.level = self
        slime.player = player
        slime.dead_image = images["slimeDead"]
        self.block_list.add(slime)
        

        for i in range(80,430,550):
            wall = Block((1610,i),images["castle"])
            self.block_list.add(wall)

        
        spring = Spring((1500,430),images["SpringDown"],player)
        self.block_list.add(spring)
        
        fly = Fly((700,-140),images["fly1"],images["fly2"])
        self.block_list.add(fly)
        
        exit_sign = Block((2590,360),images["signExit"])
        self.items_list.add(exit_sign)
