import sys
import os
from sys import argv

class Game(object):
	def __init__(self):
		self.state = []
		self.depth = 0
		self.player = ""
		self.traverselog = ""
		self.legalMoves = []
		self.gridSize = 0
		self.d1List = []
		self.d2List = []
		self.d3List = []
		self.d4List = []
		self.valueList = []
		self.mappedList = []
		self.legalMovesForMiniMax = []
		self.parentList = []
		self.visitedParentsList = []
		self.stateCopy = []
		self.dict1 = {0:15,1:14,2:13,3:12,4:11,5:10,6:9,7:8,8:7,9:6,10:5,11:4,12:3,13:2,14:1}
		self.dict2 = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O'}

		self.reverseDict1 = {15:0,14:1,13:2,12:3,11:4,10:5,9:6,8:7,7:8,6:9,5:10,4:11,3:12,2:13,1:14}
		self.reverseDict2 = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14}

		self.winList = []
		self.blockClosedFourList = []
		self.createOpenFourList = []
		self.createClosedFourList = []
		self.blockOpenThreeList = []
		self.blockClosedThreeList = []
		self.createOpenThreeList = []
		self.createClosedThreeList = []
		self.createOpenTwoList = []
		self.createClosedTwoList = []

		self.eval1 = 0
		self.eval2 = 0
		self.eval3 = 0
		self.eval4 = 0
		self.eval5 = 0
		self.eval6 = 0
		self.eval7 = 0
		self.eval8 = 0
		self.eval9 = 0
		self.eval10 = 0
		self.finalEvalValue = 0
		self.algo = 0
		self.finalEvalList = []
		self.finalMovePositions = []

	def getCurrentPositions(self,state):
		posList = []
		for i in range(0,len(state)):
			for j in range(0,len(state)):
				if ((state[i][j] == "b") or (state[i][j] == "w")):
					posList.append(str(i)+","+str(j))
		return posList

	def getAvailableLegalMovesForMiniMax(self,xpos,ypos,state):
		gridSize = len(state)
		if (xpos != 0):
			if (state[xpos-1][ypos] == "."):
				self.legalMovesForMiniMax.append(str(xpos-1)+","+str(ypos))
		if (xpos != gridSize-1):
			if (state[xpos+1][ypos] == "."):
				self.legalMovesForMiniMax.append(str(xpos+1)+","+str(ypos))
		if (ypos != 0):
			if (state[xpos][ypos-1] == "."):
				self.legalMovesForMiniMax.append(str(xpos)+","+str(ypos-1))
		if (ypos != gridSize-1):
			if (state[xpos][ypos+1] == "."):
				self.legalMovesForMiniMax.append(str(xpos)+","+str(ypos+1))

		#diagonal neighbours for corners
		if ((xpos == 0) and (ypos == 0)):
			if (state[xpos+1][ypos+1] == "."):
				self.legalMovesForMiniMax.append(str(xpos+1)+","+str(ypos+1))
		if ((xpos == gridSize-1) and (ypos == 0)):
			if (state[xpos-1][ypos+1] == "."):
				self.legalMovesForMiniMax.append(str(xpos-1)+","+str(ypos+1))
		if ((xpos == 0) and (ypos == gridSize-1)):
			if (state[xpos+1][ypos-1] == "."):
				self.legalMovesForMiniMax.append(str(xpos+1)+","+str(ypos-1))
		if ((xpos == gridSize-1) and (ypos == gridSize-1)):
			if (state[xpos-1][ypos-1] == "."):
				self.legalMovesForMiniMax.append(str(xpos-1)+","+str(ypos-1))

		#diagonal neighbours for non corner points on the boundary
		if ((xpos == 0) and (ypos != gridSize-1) and (ypos != 0)):
			if (state[xpos+1][ypos-1] == "."):
				self.legalMovesForMiniMax.append(str(xpos+1)+","+str(ypos-1))
			if (state[xpos+1][ypos+1] == "."):
				self.legalMovesForMiniMax.append(str(xpos+1)+","+str(ypos+1))
		if ((xpos == gridSize-1) and (ypos != 0) and (ypos != gridSize-1)):
			if (state[xpos-1][ypos-1] == "."):
				self.legalMovesForMiniMax.append(str(xpos-1)+","+str(ypos-1))
			if (state[xpos-1][ypos+1] == "."):
				self.legalMovesForMiniMax.append(str(xpos-1)+","+str(ypos+1))
		if ((ypos == 0) and (xpos != 0) and (xpos != gridSize-1)):
			if (state[xpos-1][ypos+1] == "."):
				self.legalMovesForMiniMax.append(str(xpos-1)+","+str(ypos+1))
			if (state[xpos+1][ypos+1] == "."):
				self.legalMovesForMiniMax.append(str(xpos+1)+","+str(ypos+1))
		if ((ypos == gridSize-1) and (xpos != 0) and (xpos != gridSize-1)):
			if (state[xpos-1][ypos-1] == "."):
				self.legalMovesForMiniMax.append(str(xpos-1)+","+str(ypos-1))
			if (state[xpos+1][ypos-1] == "."):
				self.legalMovesForMiniMax.append(str(xpos+1)+","+str(ypos-1))

		#diagonal neighbours for interior points
		if ((xpos != 0) and (xpos != gridSize-1) and (ypos != gridSize-1) and (ypos != 0)):
			if (state[xpos-1][ypos-1] == "."):
				self.legalMovesForMiniMax.append(str(xpos-1)+","+str(ypos-1))
			if (state[xpos-1][ypos+1] == "."):
				self.legalMovesForMiniMax.append(str(xpos-1)+","+str(ypos+1))
			if (state[xpos+1][ypos-1] == "."):
				self.legalMovesForMiniMax.append(str(xpos+1)+","+str(ypos-1))
			if (state[xpos+1][ypos+1] == "."):
				self.legalMovesForMiniMax.append(str(xpos+1)+","+str(ypos+1))
		
		return self.legalMovesForMiniMax

	def getAvailableLegalMoves(self,xpos,ypos,state):
		gridSize = len(state)
		if (xpos != 0):
			if (state[xpos-1][ypos] == "."):
				self.legalMoves.append(str(xpos-1)+","+str(ypos))
		if (xpos != gridSize-1):
			if (state[xpos+1][ypos] == "."):
				self.legalMoves.append(str(xpos+1)+","+str(ypos))
		if (ypos != 0):
			if (state[xpos][ypos-1] == "."):
				self.legalMoves.append(str(xpos)+","+str(ypos-1))
		if (ypos != gridSize-1):
			if (state[xpos][ypos+1] == "."):
				self.legalMoves.append(str(xpos)+","+str(ypos+1))

		#diagonal neighbours for corners
		if ((xpos == 0) and (ypos == 0)):
			if (state[xpos+1][ypos+1] == "."):
				self.legalMoves.append(str(xpos+1)+","+str(ypos+1))
		if ((xpos == gridSize-1) and (ypos == 0)):
			if (state[xpos-1][ypos+1] == "."):
				self.legalMoves.append(str(xpos-1)+","+str(ypos+1))
		if ((xpos == 0) and (ypos == gridSize-1)):
			if (state[xpos+1][ypos-1] == "."):
				self.legalMoves.append(str(xpos+1)+","+str(ypos-1))
		if ((xpos == gridSize-1) and (ypos == gridSize-1)):
			if (state[xpos-1][ypos-1] == "."):
				self.legalMoves.append(str(xpos-1)+","+str(ypos-1))

		#diagonal neighbours for non corner points on the boundary
		if ((xpos == 0) and (ypos != gridSize-1) and (ypos != 0)):
			if (state[xpos+1][ypos-1] == "."):
				self.legalMoves.append(str(xpos+1)+","+str(ypos-1))
			if (state[xpos+1][ypos+1] == "."):
				self.legalMoves.append(str(xpos+1)+","+str(ypos+1))
		if ((xpos == gridSize-1) and (ypos != 0) and (ypos != gridSize-1)):
			if (state[xpos-1][ypos-1] == "."):
				self.legalMoves.append(str(xpos-1)+","+str(ypos-1))
			if (state[xpos-1][ypos+1] == "."):
				self.legalMoves.append(str(xpos-1)+","+str(ypos+1))
		if ((ypos == 0) and (xpos != 0) and (xpos != gridSize-1)):
			if (state[xpos-1][ypos+1] == "."):
				self.legalMoves.append(str(xpos-1)+","+str(ypos+1))
			if (state[xpos+1][ypos+1] == "."):
				self.legalMoves.append(str(xpos+1)+","+str(ypos+1))
		if ((ypos == gridSize-1) and (xpos != 0) and (xpos != gridSize-1)):
			if (state[xpos-1][ypos-1] == "."):
				self.legalMoves.append(str(xpos-1)+","+str(ypos-1))
			if (state[xpos+1][ypos-1] == "."):
				self.legalMoves.append(str(xpos+1)+","+str(ypos-1))

		#diagonal neighbours for interior points
		if ((xpos != 0) and (xpos != gridSize-1) and (ypos != gridSize-1) and (ypos != 0)):
			if (state[xpos-1][ypos-1] == "."):
				self.legalMoves.append(str(xpos-1)+","+str(ypos-1))
			if (state[xpos-1][ypos+1] == "."):
				self.legalMoves.append(str(xpos-1)+","+str(ypos+1))
			if (state[xpos+1][ypos-1] == "."):
				self.legalMoves.append(str(xpos+1)+","+str(ypos-1))
			if (state[xpos+1][ypos+1] == "."):
				self.legalMoves.append(str(xpos+1)+","+str(ypos+1))
		
		return self.legalMoves

	def getDiagonalTopLeft(self,xval,yval,maxSize,state):
		list1 = []
		self.d1List = []
		while ((xval >= 0) and (yval >= 0)):
			if (((xval-1) >= 0) and ((yval-1) >= 0)):
				list1.append(str(xval-1)+","+str(yval-1))
				self.d1List.insert(0,state[xval-1][yval-1])
				xval = xval - 1
				yval = yval - 1
			else:
				break
		if len(list1) != 0:
			return list1[-1]
		else:
			list1.append(str(xval)+","+str(yval))
			self.d1List.insert(0,state[xval][yval])
			return list1[-1]

	def getDiagonalBottomRight(self,xval,yval,maxSize,state):
		list2 = []
		self.d2List = []
		while ((xval <= maxSize-1) and (yval <= maxSize-1)):
			if (((xval+1) <= (maxSize-1)) and ((yval+1) <= (maxSize-1))):
				list2.append(str(xval+1)+","+str(yval+1))
				self.d2List.insert(0,state[xval+1][yval+1])
				xval = xval + 1
				yval = yval + 1
			else:
				break

		if len(list2) != 0:
			return list2[-1]
		else:
			list2.append(str(xval)+","+str(yval))
			self.d2List.insert(0,state[xval][yval])
			return list2[-1]

	def getDiagonalTopRight(self,xval,yval,maxSize,state):
		list3 = []
		self.d3List = []
		while ((xval >= 0) and (yval <= maxSize-1)):
			if (((xval-1) >= 0) and ((yval+1) <= (maxSize-1))):
				list3.append(str(xval-1)+","+str(yval+1))
				self.d3List.insert(0,state[xval-1][yval+1])
				xval = xval - 1
				yval = yval + 1
			else:
				break

		if len(list3) != 0:
			return list3[-1]
		else:
			list3.append(str(xval)+","+str(yval))
			self.d3List.insert(0,state[xval][yval])
			return list3[-1]

	def getDiagonalBottomLeft(self,xval,yval,maxSize,state):
		list4 = []
		self.d4List = []
		while ((xval <= maxSize-1) and (yval >= 0)):
			if (((xval+1) <= (maxSize-1)) and ((yval-1) >= 0)):
				list4.append(str(xval+1)+","+str(yval-1))
				self.d4List.insert(0,state[xval+1][yval-1])
				xval = xval + 1
				yval = yval - 1
			else:
				break

		if len(list4) != 0:
			return list4[-1]
		else:
			list4.append(str(xval)+","+str(yval))
			self.d4List.insert(0,state[xval][yval])
			return list4[-1]

	def getRowLeft(self,xval,yval,maxSize):
		list5 = []
		while ((yval >= 0)):
			if ((yval - 1) >= 0):
				list5.append(str(xval)+","+str(yval-1))
				yval = yval - 1
			else:
				break

		if len(list5) != 0:
			return list5[-1]
		else:
			list5.append(str(xval)+","+str(yval))
			return list5[-1]

	def getRowRight(self,xval,yval,maxSize):
		list6 = []
		while (yval <= (maxSize-1)):
			if ((yval + 1) <= (maxSize-1)):
				list6.append(str(xval)+","+str(yval+1))
				yval = yval + 1
			else:
				break

		if len(list6) != 0:
			return list6[-1]
		else:
			list6.append(str(xval)+","+str(yval))
			return list6[-1]

	def getColumnTop(self,xval,yval,maxSize):
		list7 = []

		while ((xval >= 0)):
			if ((xval - 1) >= 0):
				list7.append(str(xval-1)+","+str(yval))
				xval = xval - 1
			else:
				break

		if len(list7) != 0:
			return list7[-1]
		else:
			list7.append(str(xval)+","+str(yval))
			return list7[-1]

	def getColumnBottom(self,xval,yval,maxSize):
		list8 = []
		while (xval <= (maxSize-1)):
			if ((xval + 1) <= (maxSize-1)):
				list8.append(str(xval+1)+","+str(yval))
				xval = xval + 1
			else:
				break

		if len(list8) != 0:
			return list8[-1]
		else:
			list8.append(str(xval)+","+str(yval))
			return list8[-1]

	def getAllEndPoints(self,xval,yval,state):
		maxSize = self.gridSize


		#current row end points
		rowLeft = self.getRowLeft(xval,yval,maxSize)

		rowRight = self.getRowRight(xval,yval,maxSize)

		#current column end points
		colTop = self.getColumnTop(xval,yval,maxSize)

		colBottom = self.getColumnBottom(xval,yval,maxSize)

		#diagonal end points
		topLeft = self.getDiagonalTopLeft(xval,yval,maxSize,state)
		bottomRight = self.getDiagonalBottomRight(xval,yval,maxSize,state)
		topRight = self.getDiagonalTopRight(xval,yval,maxSize,state)
		bottomLeft = self.getDiagonalBottomLeft(xval,yval,maxSize,state)

		masterList = []
		masterList.append(rowLeft)
		masterList.append(rowRight)
		masterList.append(colTop)
		masterList.append(colBottom)
		masterList.append(topLeft)
		masterList.append(bottomRight)
		masterList.append(topRight)
		masterList.append(bottomLeft)

		self.getEvaluationFunction(xval,yval,masterList,state)

	def  getStringForList(self,tempList):
		return ''.join(tempList)

	def checkForWin(self,colStr,rowStr,d1Str,d2Str,xval,yval,diagPos1,diagPos2):
		self.winList = []
		
		if (self.player == "w"):
			pos = rowStr.find("wwwww")
			if ((pos != -1) and (yval >= pos) and (yval <= pos+4)):
				self.winList.append(1)
			pos = colStr.find("wwwww")
			if ((pos != -1) and (xval >= pos) and (xval <= pos+4)):
				self.winList.append(1)
			pos = d1Str.find("wwwww")
			if ((pos != -1) and (diagPos1 >= pos) and (diagPos1 <= pos+4)):
				self.winList.append(1)
			pos = d2Str.find("wwwww")
			if ((pos != -1) and (diagPos2 >= pos) and (diagPos2 <= pos+4)):
				self.winList.append(1)
		else:
			pos = rowStr.find("bbbbb")
			if ((pos != -1) and (yval >= pos) and (yval <= pos+4)):
				self.winList.append(2)
			pos = colStr.find("bbbbb")
			if ((pos != -1) and (xval >= pos) and (xval <= pos+4)):
				self.winList.append(2)
			pos = d1Str.find("bbbbb")
			if ((pos != -1) and (diagPos1 >= pos) and (diagPos1 <= pos+4)):
				self.winList.append(2)
			pos = d2Str.find("bbbbb")
			if ((pos != -1) and (diagPos2 >= pos) and (diagPos2 <= pos+4)):
				self.winList.append(2)

		return self.winList

	def checkBlockClosedFour(self,colStr,rowStr,d1Str,d2Str,xval,yval,diagPos1,diagPos2):
		self.blockClosedFourList = []

		if (self.player == "w"):
			pos = rowStr.find("wbbbbw")
			if ((pos != -1) and ((yval == pos) or (yval == pos+5))):
				self.blockClosedFourList.append(1)
			pos = colStr.find("wbbbbw")
			if ((pos != -1) and ((xval == pos) or (xval == pos+5))):
				self.blockClosedFourList.append(1)
			pos = d1Str.find("wbbbbw")
			if ((pos != -1) and ((diagPos1 == pos) or (diagPos1 == pos+5))):
				self.blockClosedFourList.append(1)
			pos = d2Str.find("wbbbbw")
			if ((pos != -1) and ((diagPos2 == pos) or (diagPos2 == pos+5))):
				self.blockClosedFourList.append(1)
		else:
			pos = rowStr.find("bwwwwb")
			if ((pos != -1) and ((yval == pos) or (yval == pos+5))):
				self.blockClosedFourList.append(2)
			pos = colStr.find("bwwwwb")
			if ((pos != -1) and ((xval == pos) or (xval == pos+5))):
				self.blockClosedFourList.append(2)
			pos = d1Str.find("bwwwwb")
			if ((pos != -1) and ((diagPos1 == pos) or (diagPos1 == pos+5))):
				self.blockClosedFourList.append(2)
			pos = d2Str.find("bwwwwb")
			if ((pos != -1) and ((diagPos2 == pos) or (diagPos2 == pos+5))):
				self.blockClosedFourList.append(2)

		return self.blockClosedFourList

	def checkCreateOpenFour(self,colStr,rowStr,d1Str,d2Str,xval,yval,diagPos1,diagPos2):
		self.createOpenFourList = []

		if (self.player == "w"):
			pos = rowStr.find(".wwww.")
			if ((pos != -1) and ((yval >= pos+1) and (yval <= pos+4))):
				self.createOpenFourList.append(1)
			pos = colStr.find(".wwww.")
			if ((pos != -1) and ((xval >= pos+1) and (xval <= pos+4))):
				self.createOpenFourList.append(1)
			pos = d1Str.find(".wwww.")
			if ((pos != -1) and ((diagPos1 >= pos+1) and (diagPos1 <= pos+4))):
				self.createOpenFourList.append(1)
			pos = d2Str.find(".wwww.")
			if ((pos != -1) and ((diagPos2 >= pos+1) and (diagPos2 <= pos+4))):
				self.createOpenFourList.append(1)
		else:
			pos = rowStr.find(".bbbb.")
			if ((pos != -1) and ((yval >= pos+1) and (yval <= pos+4))):
				self.createOpenFourList.append(2)
			pos = colStr.find(".bbbb.")
			if ((pos != -1) and ((xval >= pos+1) and (xval <= pos+4))):
				self.createOpenFourList.append(2)
			pos = d1Str.find(".bbbb.")
			if ((pos != -1) and ((diagPos1 >= pos+1) and (diagPos1 <= pos+4))):
				self.createOpenFourList.append(2)
			pos = d2Str.find(".bbbb.")
			if ((pos != -1) and ((diagPos2 >= pos+1) and (diagPos2 <= pos+4))):
				self.createOpenFourList.append(2)

		return self.createOpenFourList

	def checkCreateClosedFour(self,colStr,rowStr,d1Str,d2Str,xval,yval,diagPos1,diagPos2):
		self.createClosedFourList = []

		if (self.player == "w"):

			pos1 = rowStr.find("wwwwb")
			pos2 = rowStr.find("bwwww")

			if (((pos1 != -1) and ((yval >= pos1) and (yval <= pos1+3))) or ((pos2 != -1) and ((yval >= pos2+1) and (yval <= pos2+4)))):
				self.createClosedFourList.append(1)
			
			pos1 = colStr.find("wwwwb")
			pos2 = colStr.find("bwwww")
			if (((pos1 != -1) and ((xval >= pos1) and (xval <= pos1+3))) or ((pos2 != -1) and ((xval >= pos2+1) and (xval <= pos2+4)))):
				self.createClosedFourList.append(1)

			pos1 = d1Str.find("wwwwb")
			pos2 = d1Str.find("bwwww")
			if (((pos1 != -1) and ((diagPos1 >= pos1) and (diagPos1 <= pos1+3))) or ((pos2 != -1) and ((diagPos1 >= pos2+1) and (diagPos1 <= pos2+4)))):
				self.createClosedFourList.append(1)
			
			pos1 = d2Str.find("wwwwb")
			pos2 = d2Str.find("bwwww")
			if (((pos1 != -1) and ((diagPos2 >= pos1) and (diagPos2 <= pos1+3))) or ((pos2 != -1) and ((diagPos2 >= pos2+1) and (diagPos2 <= pos2+4)))):
				self.createClosedFourList.append(1)

			#Cases when board boundry can block instead of opponent
			pos3 = rowStr.find("wwww.")
			pos4 = rowStr.find(".wwww")

			if ((pos3 == 0) and (yval >= pos3) and (yval <= pos3+3)):
				self.createClosedFourList.append(1)

			length = len(rowStr)
			if ((length-5) >= 0):
				if ((pos4 == rowStr[length-5]) and (yval >= pos4+1) and (yval <= pos4+4)):
					self.createClosedFourList.append(1)

			pos3 = colStr.find("wwww.")
			pos4 = colStr.find(".wwww")

			if ((pos3 == 0) and (xval >= pos3) and (xval <= pos3+3)):
				self.createClosedFourList.append(1)

			length = len(colStr)
			if((length-5) >= 0):
				if ((pos4 == rowStr[length-5]) and (xval >= pos4+1) and (xval <= pos4+4)):
					self.createClosedFourList.append(1)

			pos3 = d1Str.find("wwww.")
			pos4 = d1Str.find(".wwww")

			if ((pos3 == 0) and (diagPos1 >= pos3) and (diagPos1 <= pos3+3)):
				self.createClosedFourList.append(1)

			length = len(d1Str)
			if((length-5)>=0):
				if ((pos4 == d1Str[length-5]) and (diagPos1 >= pos4+1) and (diagPos1 <= pos4+4)):
					self.createClosedFourList.append(1)

			pos3 = d2Str.find("wwww.")
			pos4 = d2Str.find(".wwww")

			if ((pos3 == 0) and (diagPos2 >= pos3) and (diagPos2 <= pos3+3)):
				self.createClosedFourList.append(1)

			length = len(d2Str)
			if((length-5) >= 0):
				if ((pos4 == d2Str[length-5]) and (diagPos2 >= pos4+1) and (diagPos2 <= pos4+4)):
					self.createClosedFourList.append(1)

		else:
			pos1 = rowStr.find("bbbbw")
			pos2 = rowStr.find("wbbbb")

			if (((pos1 != -1) and ((yval >= pos1) and (yval <= pos1+3))) or ((pos2 != -1) and ((yval >= pos2+1) and (yval <= pos2+4)))):
				self.createClosedFourList.append(2)
			
			pos1 = colStr.find("bbbbw")
			pos2 = colStr.find("wbbbb")
			if (((pos1 != -1) and ((xval >= pos1) and (xval <= pos1+3))) or ((pos2 != -1) and ((xval >= pos2+1) and (xval <= pos2+4)))):
				self.createClosedFourList.append(2)

			pos1 = d1Str.find("bbbbw")
			pos2 = d1Str.find("wbbbb")
			if (((pos1 != -1) and ((diagPos1 >= pos1) and (diagPos1 <= pos1+3))) or ((pos2 != -1) and ((diagPos1 >= pos2+1) and (diagPos1 <= pos2+4)))):
				self.createClosedFourList.append(2)
			
			pos1 = d2Str.find("bbbbw")
			pos2 = d2Str.find("wbbbb")
			if (((pos1 != -1) and ((diagPos2 >= pos1) and (diagPos2 <= pos1+3))) or ((pos2 != -1) and ((diagPos2 >= pos2+1) and (diagPos2 <= pos2+4)))):
				self.createClosedFourList.append(2)

			#Cases when board boundry can block instead of opponent
			pos3 = rowStr.find("bbbb.")
			pos4 = rowStr.find(".bbbb")

			if ((pos3 == 0) and (yval >= pos3) and (yval <= pos3+3)):
				self.createClosedFourList.append(2)

			length = len(rowStr)
			if((length-5) >= 0):
				if ((pos4 == rowStr[length-5]) and (yval >= pos4+1) and (yval <= pos4+4)):
					self.createClosedFourList.append(2)

			pos3 = colStr.find("bbbb.")
			pos4 = colStr.find(".bbbb")

			if ((pos3 == 0) and (xval >= pos3) and (xval <= pos3+3)):
				self.createClosedFourList.append(2)

			length = len(colStr)
			if((length-5) >= 0):
				if ((pos4 == rowStr[length-5]) and (xval >= pos4+1) and (xval <= pos4+4)):
					self.createClosedFourList.append(2)

			pos3 = d1Str.find("bbbb.")
			pos4 = d1Str.find(".bbbb")

			if ((pos3 == 0) and (diagPos1 >= pos3) and (diagPos1 <= pos3+3)):
				self.createClosedFourList.append(2)

			length = len(d1Str)
			if((length-5) >= 0):
				if ((pos4 == d1Str[length-5]) and (diagPos1 >= pos4+1) and (diagPos1 <= pos4+4)):
					self.createClosedFourList.append(2)

			pos3 = d2Str.find("bbbb.")
			pos4 = d2Str.find(".bbbb")

			if ((pos3 == 0) and (diagPos2 >= pos3) and (diagPos2 <= pos3+3)):
				self.createClosedFourList.append(2)

			length = len(d2Str)
			if((length-5) >= 0):
				if ((pos4 == d2Str[length-5]) and (diagPos2 >= pos4+1) and (diagPos2 <= pos4+4)):
					self.createClosedFourList.append(2)

		return self.createClosedFourList

	def checkBlockOpenThree(self,colStr,rowStr,d1Str,d2Str,xval,yval,diagPos1,diagPos2):
		self.blockOpenThreeList = []

		if (self.player == "w"):
			pos1 = rowStr.find("wbbb")
			pos2 = rowStr.find("bbbw")

			if (((pos1 != -1) and (yval == pos1)) or ((pos2 != -1) and (yval == pos2))):
				self.blockOpenThreeList.append(1)
			
			pos1 = colStr.find("wbbb")
			pos2 = colStr.find("bbbw")
			if (((pos1 != -1) and (xval == pos1)) or ((pos2 != -1) and (xval == pos2))):
				self.blockOpenThreeList.append(1)

			pos1 = d1Str.find("wbbb")
			pos2 = d1Str.find("bbbw")
			if (((pos1 != -1) and (diagPos1 == pos1)) or ((pos2 != -1) and (diagPos1 == pos2))):
				self.blockOpenThreeList.append(1)
			
			pos1 = d2Str.find("wbbb")
			pos2 = d2Str.find("bbbw")
			if (((pos1 != -1) and (diagPos2 == pos1)) or ((pos2 != -1) and (diagPos2 == pos2))):
				self.blockOpenThreeList.append(1)
		else:
			pos1 = rowStr.find("bwww")
			pos2 = rowStr.find("wwwb")

			if (((pos1 != -1) and (yval == pos1)) or ((pos2 != -1) and (yval == pos2))):
				self.blockOpenThreeList.append(2)
			
			pos1 = colStr.find("bwww")
			pos2 = colStr.find("wwwb")
			if (((pos1 != -1) and (xval == pos1)) or ((pos2 != -1) and (xval == pos2))):
				self.blockOpenThreeList.append(2)

			pos1 = d1Str.find("bwww")
			pos2 = d1Str.find("wwwb")
			if (((pos1 != -1) and (diagPos1 == pos1)) or ((pos2 != -1) and (diagPos1 == pos2))):
				self.blockOpenThreeList.append(2)
			
			pos1 = d2Str.find("bwww")
			pos2 = d2Str.find("wwwb")
			if (((pos1 != -1) and (diagPos2 == pos1)) or ((pos2 != -1) and (diagPos2 == pos2))):
				self.blockOpenThreeList.append(2)

		return self.blockOpenThreeList

	def checkBlockClosedThree(self,colStr,rowStr,d1Str,d2Str,xval,yval,diagPos1,diagPos2):
		self.blockClosedThreeList = []

		if (self.player == "w"):
			pos = rowStr.find("wbbbw")
			if ((pos != -1) and ((yval == pos) or (yval == pos+4))):
				self.blockClosedThreeList.append(1)
			
			pos = colStr.find("wbbbw")
			if ((pos != -1) and ((xval == pos) or (xval == pos+4))):
				self.blockClosedThreeList.append(1)

			pos = d1Str.find("wbbbw")
			if ((pos != -1) and ((diagPos1 == pos) or (diagPos1 == pos+4))):
				self.blockClosedThreeList.append(1)
			
			pos = d2Str.find("wbbbw")
			if ((pos != -1) and ((diagPos2 == pos) or (diagPos2 == pos+4))):
				self.blockClosedThreeList.append(1)

		else:
			pos = rowStr.find("bwwwb")
			if ((pos != -1) and ((yval == pos) or (yval == pos+4))):
				self.blockClosedThreeList.append(2)
			
			pos = colStr.find("bwwwb")
			if ((pos != -1) and ((xval == pos) or (xval == pos+4))):
				self.blockClosedThreeList.append(2)

			pos = d1Str.find("bwwwb")
			if ((pos != -1) and ((diagPos1 == pos) or (diagPos1 == pos+4))):
				self.blockClosedThreeList.append(2)
			
			pos = d2Str.find("bwwwb")
			if ((pos != -1) and ((diagPos2 == pos) or (diagPos2 == pos+4))):
				self.blockClosedThreeList.append(2)

		return self.blockClosedThreeList

	def checkCreateOpenThree(self,colStr,rowStr,d1Str,d2Str,xval,yval,diagPos1,diagPos2):
		self.createOpenThreeList = []

		if (self.player == "w"):
			pos = rowStr.find(".www.")
			if ((pos != -1) and ((yval >= pos+1) and (yval <= pos+3))):
				self.createOpenThreeList.append(1)
			pos = colStr.find(".www.")
			if ((pos != -1) and ((xval >= pos+1) and (xval <= pos+3))):
				self.createOpenThreeList.append(1)
			pos = d1Str.find(".www.")
			if ((pos != -1) and ((diagPos1 >= pos+1) and (diagPos1 <= pos+3))):
				self.createOpenThreeList.append(1)
			pos = d2Str.find(".www.")
			if ((pos != -1) and ((diagPos2 >= pos+1) and (diagPos2 <= pos+3))):
				self.createOpenThreeList.append(1)
		else:
			pos = rowStr.find(".bbb.")
			if ((pos != -1) and ((yval >= pos+1) and (yval <= pos+3))):
				self.createOpenThreeList.append(2)
			pos = colStr.find(".bbb.")
			if ((pos != -1) and ((xval >= pos+1) and (xval <= pos+3))):
				self.createOpenThreeList.append(2)
			pos = d1Str.find(".bbb.")
			if ((pos != -1) and ((diagPos1 >= pos+1) and (diagPos1 <= pos+3))):
				self.createOpenThreeList.append(2)
			pos = d2Str.find(".bbb.")
			if ((pos != -1) and ((diagPos2 >= pos+1) and (diagPos2 <= pos+3))):
				self.createOpenThreeList.append(2)

		return self.createOpenThreeList

	def checkCreateClosedThree(self,colStr,rowStr,d1Str,d2Str,xval,yval,diagPos1,diagPos2):
		self.createClosedThreeList = []

		if (self.player == "w"):
			pos1 = rowStr.find("wwwb")
			pos2 = rowStr.find("bwww")
			if (((pos1 != -1) and ((yval >= pos1) and (yval <= pos1+2))) or ((pos2 != -1) and ((yval >= pos2+1) and (yval <= pos2+3)))):
				self.createClosedThreeList.append(1)
			
			pos1 = colStr.find("wwwb")
			pos2 = colStr.find("bwww")
			if (((pos1 != -1) and ((xval >= pos1) and (xval <= pos1+2))) or ((pos2 != -1) and ((xval >= pos2+1) and (xval <= pos2+3)))):
				self.createClosedThreeList.append(1)

			pos1 = d1Str.find("wwwb")
			pos2 = d1Str.find("bwww")
			if (((pos1 != -1) and ((diagPos1 >= pos1) and (diagPos1 <= pos1+2))) or ((pos2 != -1) and ((diagPos1 >= pos2+1) and (diagPos1 <= pos2+3)))):
				self.createClosedThreeList.append(1)
			
			pos1 = d2Str.find("wwwb")
			pos2 = d2Str.find("bwww")
			if (((pos1 != -1) and ((diagPos2 >= pos1) and (diagPos2 <= pos1+2))) or ((pos2 != -1) and ((diagPos2 >= pos2+1) and (diagPos2 <= pos2+3)))):
				self.createClosedThreeList.append(1)

			#Cases when board boundry can block instead of opponent
			pos3 = rowStr.find("www.")
			pos4 = rowStr.find(".www")

			if ((pos3 == 0) and (yval >= pos3) and (yval <= pos3+2)):
				self.createClosedThreeList.append(1)

			length = len(rowStr)
			if ((length-4) >=0):
				if ((pos4 == rowStr[length-4]) and (yval >= pos4+1) and (yval <= pos4+3)):
					self.createClosedThreeList.append(1)

			pos3 = colStr.find("www.")
			pos4 = colStr.find(".www")

			if ((pos3 == 0) and (xval >= pos3) and (xval <= pos3+2)):
				self.createClosedThreeList.append(1)

			length = len(colStr)
			if ((length - 4) >= 0):
				if ((pos4 == rowStr[length-4]) and (xval >= pos4+1) and (xval <= pos4+3)):
					self.createClosedThreeList.append(1)

			pos3 = d1Str.find("www.")
			pos4 = d1Str.find(".www")

			if ((pos3 == 0) and (diagPos1 >= pos3) and (diagPos1 <= pos3+2)):
				self.createClosedThreeList.append(1)

			length = len(d1Str)
			if ((length - 4) >= 0):
				if ((pos4 == d1Str[length-4]) and (diagPos1 >= pos4+1) and (diagPos1 <= pos4+3)):
					self.createClosedThreeList.append(1)

			pos3 = d2Str.find("www.")
			pos4 = d2Str.find(".www")

			if ((pos3 == 0) and (diagPos2 >= pos3) and (diagPos2 <= pos3+2)):
				self.createClosedThreeList.append(1)

			length = len(d2Str)
			if ((length - 4) >= 0):
				if ((pos4 == d2Str[length-4]) and (diagPos2 >= pos4+1) and (diagPos2 <= pos4+3)):
					self.createClosedThreeList.append(1)

		else:
			pos1 = rowStr.find("bbbw")
			pos2 = rowStr.find("wbbb")
			if (((pos1 != -1) and ((yval >= pos1) and (yval <= pos1+2))) or ((pos2 != -1) and ((yval >= pos2+1) and (yval <= pos2+3)))):
				self.createClosedThreeList.append(2)
			
			pos1 = colStr.find("bbbw")
			pos2 = colStr.find("wbbb")
			if (((pos1 != -1) and ((xval >= pos1) and (xval <= pos1+2))) or ((pos2 != -1) and ((xval >= pos2+1) and (xval <= pos2+3)))):
				self.createClosedThreeList.append(2)

			pos1 = d1Str.find("bbbw")
			pos2 = d1Str.find("wbbb")
			if (((pos1 != -1) and ((diagPos1 >= pos1) and (diagPos1 <= pos1+2))) or ((pos2 != -1) and ((diagPos1 >= pos2+1) and (diagPos1 <= pos2+3)))):
				self.createClosedThreeList.append(2)
			
			pos1 = d2Str.find("bbbw")
			pos2 = d2Str.find("wbbb")
			if (((pos1 != -1) and ((diagPos2 >= pos1) and (diagPos2 <= pos1+2))) or ((pos2 != -1) and ((diagPos2 >= pos2+1) and (diagPos2 <= pos2+3)))):
				self.createClosedThreeList.append(2)

			#Cases when board boundry can block instead of opponent
			pos3 = rowStr.find("bbb.")
			pos4 = rowStr.find(".bbb")

			if ((pos3 == 0) and (yval >= pos3) and (yval <= pos3+2)):
				self.createClosedThreeList.append(2)

			length = len(rowStr)
			if ((length - 4) >= 0):
				if ((pos4 == rowStr[length-4]) and (yval >= pos4+1) and (yval <= pos4+3)):
					self.createClosedThreeList.append(2)

			pos3 = colStr.find("bbb.")
			pos4 = colStr.find(".bbb")

			if ((pos3 == 0) and (xval >= pos3) and (xval <= pos3+2)):
				self.createClosedThreeList.append(2)

			length = len(colStr)
			if ((length - 4) >= 0):
				if ((pos4 == rowStr[length-4]) and (xval >= pos4+1) and (xval <= pos4+3)):
					self.createClosedThreeList.append(2)

			pos3 = d1Str.find("bbb.")
			pos4 = d1Str.find(".bbb")

			if ((pos3 == 0) and (diagPos1 >= pos3) and (diagPos1 <= pos3+2)):
				self.createClosedThreeList.append(2)

			length = len(d1Str)
			if ((length - 4) >= 0):
				if ((pos4 == d1Str[length-4]) and (diagPos1 >= pos4+1) and (diagPos1 <= pos4+3)):
					self.createClosedThreeList.append(2)

			pos3 = d2Str.find("bbb.")
			pos4 = d2Str.find(".bbb")

			if ((pos3 == 0) and (diagPos2 >= pos3) and (diagPos2 <= pos3+2)):
				self.createClosedThreeList.append(2)

			length = len(d2Str)
			if ((length - 4) >= 0):
				if ((pos4 == d2Str[length-4]) and (diagPos2 >= pos4+1) and (diagPos2 <= pos4+3)):
					self.createClosedThreeList.append(2)

		return self.createClosedThreeList

	def checkCreateOpenTwo(self,colStr,rowStr,d1Str,d2Str,xval,yval,diagPos1,diagPos2):
		self.createOpenTwoList = []

		if (self.player == "w"):
			pos = rowStr.find(".ww.")
			if ((pos != -1) and ((yval >= pos+1) and (yval <= pos+2))):
				self.createOpenTwoList.append(1)
			pos = colStr.find(".ww.")
			if ((pos != -1) and ((xval >= pos+1) and (xval <= pos+2))):
				self.createOpenTwoList.append(1)
			pos = d1Str.find(".ww.")
			if ((pos != -1) and ((diagPos1 >= pos+1) and (diagPos1 <= pos+2))):
				self.createOpenTwoList.append(1)
			pos = d2Str.find(".ww.")
			if ((pos != -1) and ((diagPos2 >= pos+1) and (diagPos2 <= pos+2))):
				self.createOpenTwoList.append(1)
		else:
			pos = rowStr.find(".bb.")
			if ((pos != -1) and ((yval >= pos+1) and (yval <= pos+2))):
				self.createOpenTwoList.append(2)
			pos = colStr.find(".bb.")
			if ((pos != -1) and ((xval >= pos+1) and (xval <= pos+2))):
				self.createOpenTwoList.append(2)
			pos = d1Str.find(".bb.")
			if ((pos != -1) and ((diagPos1 >= pos+1) and (diagPos1 <= pos+2))):
				self.createOpenTwoList.append(2)
			pos = d2Str.find(".bb.")
			if ((pos != -1) and ((diagPos2 >= pos+1) and (diagPos2 <= pos+2))):
				self.createOpenTwoList.append(2)

		return self.createOpenTwoList

	def checkCreateClosedTwo(self,colStr,rowStr,d1Str,d2Str,xval,yval,diagPos1,diagPos2):
		self.createClosedTwoList = []

		if (self.player == "w"):
			pos1 = rowStr.find("wwb")
			pos2 = rowStr.find("bww")
			if (((pos1 != -1) and ((yval >= pos1) and (yval <= pos1+1))) or ((pos2 != -1) and ((yval >= pos2+1) and (yval <= pos2+2)))):
				self.createClosedTwoList.append(1)
			
			pos1 = colStr.find("wwb")
			pos2 = colStr.find("bww")
			if (((pos1 != -1) and ((xval >= pos1) and (xval <= pos1+1))) or ((pos2 != -1) and ((xval >= pos2+1) and (xval <= pos2+2)))):
				self.createClosedTwoList.append(1)

			pos1 = d1Str.find("wwb")
			pos2 = d1Str.find("bww")
			if (((pos1 != -1) and ((diagPos1 >= pos1) and (diagPos1 <= pos1+1))) or ((pos2 != -1) and ((diagPos1 >= pos2+1) and (diagPos1 <= pos2+2)))):
				self.createClosedTwoList.append(1)
			
			pos1 = d2Str.find("wwb")
			pos2 = d2Str.find("bww")
			if (((pos1 != -1) and ((diagPos2 >= pos1) and (diagPos2 <= pos1+1))) or ((pos2 != -1) and ((diagPos2 >= pos2+1) and (diagPos2 <= pos2+2)))):
				self.createClosedTwoList.append(1)

			#Cases when board boundry can block instead of opponent
			pos3 = rowStr.find("ww.")
			pos4 = rowStr.find(".ww")

			if ((pos3 == 0) and (yval >= pos3) and (yval <= pos3+1)):
				self.createClosedTwoList.append(1)

			length = len(rowStr)
			if ((length - 3) >= 0):
				if ((pos4 == rowStr[length-3]) and (yval >= pos4+1) and (yval <= pos4+2)):
					self.createClosedTwoList.append(1)

			pos3 = colStr.find("ww.")
			pos4 = colStr.find(".ww")

			if ((pos3 == 0) and (xval >= pos3) and (xval <= pos3+1)):
				self.createClosedTwoList.append(1)

			length = len(colStr)
			if ((length - 3) >= 0):
				if ((pos4 == rowStr[length-3]) and (xval >= pos4+1) and (xval <= pos4+2)):
					self.createClosedTwoList.append(1)

			pos3 = d1Str.find("ww.")
			pos4 = d1Str.find(".ww")

			if ((pos3 == 0) and (diagPos1 >= pos3) and (diagPos1 <= pos3+1)):
				self.createClosedTwoList.append(1)

			length = len(d1Str)
			if ((length - 3) >= 0):
				if ((pos4 == d1Str[length-3]) and (diagPos1 >= pos4+1) and (diagPos1 <= pos4+2)):
					self.createClosedTwoList.append(1)

			pos3 = d2Str.find("ww.")
			pos4 = d2Str.find(".ww")

			if ((pos3 == 0) and (diagPos2 >= pos3) and (diagPos2 <= pos3+1)):
				self.createClosedTwoList.append(1)

			length = len(d2Str)
			if ((length - 3) >= 0):
				if ((pos4 == d2Str[length-3]) and (diagPos2 >= pos4+1) and (diagPos2 <= pos4+2)):
					self.createClosedTwoList.append(1)
		else:

			pos1 = rowStr.find("bbw")
			pos2 = rowStr.find("wbb")
			if (((pos1 != -1) and ((yval >= pos1) and (yval <= pos1+1))) or ((pos2 != -1) and ((yval >= pos2+1) and (yval <= pos2+2)))):
				self.createClosedTwoList.append(2)
			
			pos1 = colStr.find("bbw")
			pos2 = colStr.find("wbb")
			if (((pos1 != -1) and ((xval >= pos1) and (xval <= pos1+1))) or ((pos2 != -1) and ((xval >= pos2+1) and (xval <= pos2+2)))):
				self.createClosedTwoList.append(2)

			pos1 = d1Str.find("bbw")
			pos2 = d1Str.find("wbb")
			if (((pos1 != -1) and ((diagPos1 >= pos1) and (diagPos1 <= pos1+1))) or ((pos2 != -1) and ((diagPos1 >= pos2+1) and (diagPos1 <= pos2+2)))):
				self.createClosedTwoList.append(2)
			
			pos1 = d2Str.find("bbw")
			pos2 = d2Str.find("wbb")
			if (((pos1 != -1) and ((diagPos2 >= pos1) and (diagPos2 <= pos1+1))) or ((pos2 != -1) and ((diagPos2 >= pos2+1) and (diagPos2 <= pos2+2)))):
				self.createClosedTwoList.append(2)

			#Cases when board boundry can block instead of opponent
			pos3 = rowStr.find("bb.")
			pos4 = rowStr.find(".bb")

			if ((pos3 == 0) and (yval >= pos3) and (yval <= pos3+1)):
				self.createClosedTwoList.append(2)

			length = len(rowStr)
			if ((length - 3) >= 0):
				if ((pos4 == rowStr[length-3]) and (yval >= pos4+1) and (yval <= pos4+2)):
					self.createClosedTwoList.append(2)

			pos3 = colStr.find("bb.")
			pos4 = colStr.find(".bb")

			if ((pos3 == 0) and (xval >= pos3) and (xval <= pos3+1)):
				self.createClosedTwoList.append(2)

			length = len(colStr)
			if ((length - 3) >= 0):
				if ((pos4 == rowStr[length-3]) and (xval >= pos4+1) and (xval <= pos4+2)):
					self.createClosedTwoList.append(2)

			pos3 = d1Str.find("bb.")
			pos4 = d1Str.find(".bb")

			if ((pos3 == 0) and (diagPos1 >= pos3) and (diagPos1 <= pos3+1)):
				self.createClosedTwoList.append(2)

			length = len(d1Str)
			if ((length - 3) >= 0):
				if ((pos4 == d1Str[length-3]) and (diagPos1 >= pos4+1) and (diagPos1 <= pos4+2)):
					self.createClosedTwoList.append(2)

			pos3 = d2Str.find("bb.")
			pos4 = d2Str.find(".bb")

			if ((pos3 == 0) and (diagPos2 >= pos3) and (diagPos2 <= pos3+1)):
				self.createClosedTwoList.append(2)

			length = len(d2Str)
			if ((length - 3) >= 0):
				if ((pos4 == d2Str[length-3]) and (diagPos2 >= pos4+1) and (diagPos2 <= pos4+2)):
					self.createClosedTwoList.append(2)

		return 	self.createClosedTwoList
		
	def computeFinalEvalValues(self,list1,list2,list3,list4,list5,list6,list7,list8,list9,list10,xval,yval):
		
		if(self.player == "w"):
			self.eval1 = list1.count(1)*50000
			self.eval2 = list2.count(1)*10000
			self.eval3 = list3.count(1)*5000
			self.eval4 = list4.count(1)*1000
			self.eval5 = list5.count(1)*500
			self.eval6 = list6.count(1)*100
			self.eval7 = list7.count(1)*50
			self.eval8 = list8.count(1)*10
			self.eval9 = list9.count(1)*5
			self.eval10= list10.count(1)*1
		else:
			self.eval1 = list1.count(2) * -50000
			self.eval2 = list2.count(2) * -10000
			self.eval3 = list3.count(2) * -5000
			self.eval4 = list4.count(2) * -1000
			self.eval5 = list5.count(2) * -500
			self.eval6 = list6.count(2) * -100
			self.eval7 = list7.count(2) * -50
			self.eval8 = list8.count(2) * -10
			self.eval9 = list9.count(2) * -5
			self.eval10 = list10.count(2) * -1

		self.finalEvalValue = (self.eval1+self.eval2+self.eval3+self.eval4+self.eval5+self.eval6+self.eval7+self.eval8+self.eval9+self.eval10)
		self.finalEvalList.append(int(self.finalEvalValue))

	def checkPattern(self,xval,yval,masterList,state):
		maxSize = self.gridSize

		originalVal = state[xval][yval]
		state[xval][yval] = self.player

		#check column values
		value1 = masterList[2].split(",")
		value2 = masterList[3].split(",")

		#check row values
		value3 = masterList[0].split(",")
		value4 = masterList[1].split(",")

		#check diagonal 1 values
		value5 = masterList[4].split(",")
		value6 = masterList[5].split(",")

		#check diagonal 2 values
		value7 = masterList[6].split(",")
		value8 = masterList[7].split(",")
		
		colTopx = int(value1[0])
		colBottomx = int(value2[0])

		rowLefty = int(value3[1])
		rowRighty = int(value4[1])

		d1Topx = int(value5[0])
		d1Bottomx = int(value6[0])

		d2Topx = int(value7[0])
		d2Bottomx = int(value8[0])

		colList = []
		rowList = []

		currPos = state[xval][yval].split()

		for i in range(colTopx,colBottomx+1):
			colList.append(state[i][yval])
		for i in range(rowLefty,rowRighty+1):
			rowList.append(state[xval][i])
		
		if len(self.d1List) == 1 and len(self.d2List) == 1 and (xval == 0 or xval == maxSize-1) and (yval == 0 or yval == maxSize-1):
			diagonal1 = self.d1List
		elif len(self.d1List) == 1 and len(self.d2List) == 1 and (xval != 0 or xval != maxSize-1) and (yval != 0 or yval != maxSize-1):
			diagonal1 = self.d1List + currPos
		else:
			diagonal1 = self.d1List + currPos + self.d2List


		if len(self.d3List) == 1 and len(self.d4List) == 1 and (xval == 0 or xval == maxSize-1) and (yval == 0 or yval == maxSize-1):
			diagonal2 = self.d3List
		elif len(self.d3List) == 1 and len(self.d4List) == 1 and (xval != 0 or xval != maxSize-1) and (yval != 0 or yval != maxSize-1):
			diagonal2 = self.d3List + currPos
		else:
			diagonal2 = self.d3List +currPos + self.d4List

		diagPos1 = len(self.d1List)
		diagPos2 = len(self.d3List)

		#set it back
		state[xval][yval] = originalVal

		colStr = self.getStringForList(colList)
		rowStr = self.getStringForList(rowList)
		d1Str = self.getStringForList(diagonal1)
		d2Str = self.getStringForList(diagonal2)

		#Replace * if any
		colStr = colStr.replace("*",".")
		rowStr = rowStr.replace("*", ".")
		d1Str = d1Str.replace("*", ".")
		d2Str = d2Str.replace("*", ".")

		list1 = self.checkForWin(colStr,rowStr,d1Str,d2Str,xval,yval,diagPos1,diagPos2)
		list2 = self.checkBlockClosedFour(colStr,rowStr,d1Str,d2Str,xval,yval,diagPos1,diagPos2)
		list3 = self.checkCreateOpenFour(colStr,rowStr,d1Str,d2Str,xval,yval,diagPos1,diagPos2)
		list4 = self.checkCreateClosedFour(colStr,rowStr,d1Str,d2Str,xval,yval,diagPos1,diagPos2)
		list5 = self.checkBlockOpenThree(colStr,rowStr,d1Str,d2Str,xval,yval,diagPos1,diagPos2)
		list6 = self.checkBlockClosedThree(colStr,rowStr,d1Str,d2Str,xval,yval,diagPos1,diagPos2)
		list7 = self.checkCreateOpenThree(colStr,rowStr,d1Str,d2Str,xval,yval,diagPos1,diagPos2)
		list8 = self.checkCreateClosedThree(colStr,rowStr,d1Str,d2Str,xval,yval,diagPos1,diagPos2)
		list9 = self.checkCreateOpenTwo(colStr,rowStr,d1Str,d2Str,xval,yval,diagPos1,diagPos2)
		list10 = self.checkCreateClosedTwo(colStr,rowStr,d1Str,d2Str,xval,yval,diagPos1,diagPos2)

		self.computeFinalEvalValues(list1,list2,list3,list4,list5,list6,list7,list8,list9,list10,xval,yval)
			

	def getEvaluationFunction(self,xval,yval,masterList,state):
		self.checkPattern(xval,yval,masterList,state)

	def calculateBestMove(self,moves,state):
		self.finalMovePositions = []

		for i in range(0,len(moves)):
			valuePair = moves[i].split(",")
			xval = int(valuePair[0])
			yval = int(valuePair[1])
			if (state[xval][yval] == "."):
				self.finalMovePositions.append(str(xval)+","+str(yval))
				self.getAllEndPoints(xval,yval,state)

	def writeNextState(self,nextMovex,nextMovey,state):
		state[nextMovex][nextMovey] = self.player
		outFile = open("next_state.txt","w")
		for i in range(0,len(state)):
			for j in range(0,len(state)):
				outFile.write("%s" %state[i][j])
			outFile.write("\n")

	def getLegalMoves(self,state):
		currentPositions = self.getCurrentPositions(state)
		legalAvailableMoves = []

		for i in range(0,len(currentPositions)):
			value = currentPositions[i]
			pos = value.split(",")
			xpos = int(pos[0])
			ypos = int(pos[1])
			legalAvailableMoves = self.getAvailableLegalMoves(xpos,ypos,state)
			legalAvailableMoves = list(set(legalAvailableMoves))

		return legalAvailableMoves
		
	def sortAlphanumericList(self,aList):
		return ''.join(sorted(aList.rstrip().split(',')))
		
	def getNextMove(self,state,move,player):
		availList = []
		self.mappedList = []

		if (move == "root"):
			availList = self.getLegalMoves(state)
		else:
			xval = int(move.split(",")[0])
			yval = int(move.split(",")[1])

			#availList = self.getAvailableLegalMovesForMiniMax(xval,yval,state)
			availList = self.getLegalMoves(state)


		xlist = []
		ylist = []
		newlist1 = []
		newlist2 = []

		if (len(availList) == 0):
			self.legalMoves = []
			return move
		else:
			for i in range(0,len(availList)):
				xlist.append(int(availList[i].split(",")[0]))
				ylist.append(int(availList[i].split(",")[1]))

			best_y = min(ylist)

			for i in range(0,len(availList)):
				if (int(availList[i].split(",")[1]) == best_y):
					newlist1.append(str(availList[i].split(",")[0])+","+str(best_y))

			for i in range(0,len(newlist1)):
				newlist2.append(int(newlist1[i].split(",")[0]))


			best_x = max(newlist2)
			state[best_x][best_y] = player
			pos = str(best_x)+","+str(best_y)
			self.legalMoves = []
			return pos

	def getMappedPosition(self,point):
		
		if (point == "root"):
			return "root"

		mapx = int(point.split(",")[0])
		mapy = int(point.split(",")[1])

		mappedValx = str(self.dict2[mapy])
		mappedValy = str(self.dict1[mapx])

		return mappedValx+mappedValy

	def minimax(self,state,player,depth,move):
		value = ""
		if (move == "root"):
			value = "-Infinity"
			self.traverselog.write("root"+","+str(depth)+","+str(value))
			self.traverselog.write("\n")

		nextPos = self.getNextMove(state,move,player)
		parent = move
		move = nextPos
		#push into a parent list
		if not parent in self.parentList:
			self.parentList.append(parent)

		parentMapped = self.getMappedPosition(parent)
		pointMapped = self.getMappedPosition(move)

		#This is the case where all moves for the current parent are exausted
		if(parent == move):
			if (parent == "root"):
				return
			self.visitedParentsList.append(move)
			for i in range(0,len(state)):
				for j in range(0,len(state)):
					if (state[i][j] == "*"):
						state[i][j] = "."

			#state[int(move.split(",")[0])][int(move.split(",")[1])] = "*"
			for i in range(0,len(self.visitedParentsList)):
				state[int(self.visitedParentsList[i].split(",")[0])][int(self.visitedParentsList[i].split(",")[1])] = "*"
			if(len(self.getLegalMoves(state)) == 0):
				for i in range(0, len(state)):
					for j in range(0, len(state)):
						if ((i != int(move.split(",")[0])) and (j != int(move.split(",")[1]))):
							if(state[i][j] == "*"):
								state[i][j] = "."
			copyMove = move
			self.parentList.remove(move)
			parent = self.parentList[-1]

			parentMapped = self.getMappedPosition(parent)
			pointMapped = self.getMappedPosition(copyMove)

			if (player == "w"):
				self.player = "b"
			else:
				self.player = "w"

			nextPos = self.getNextMove(state,parent,player)
			move = nextPos
			#state[int(copyMove.split(",")[0])][int(copyMove.split(",")[1])] = "."
			for i in range(0, len(self.visitedParentsList)):
				state[int(self.visitedParentsList[i].split(",")[0])][int(self.visitedParentsList[i].split(",")[1])] = "."
			depth = depth-1

			self.traverselog.write(parentMapped + "," + str(depth) + "," + str(value))
			self.traverselog.write("\n")

		#parentMapped = self.getMappedPosition(parent)
		#pointMapped = self.getMappedPosition(move)
		mapx = int(move.split(",")[0])
		mapy = int(move.split(",")[1])
		# mappedValx = str(self.dict2[mapy])
		# mappedValy = str(self.dict1[mapx])

		depth = depth+1

		if (player == self.player):
			#means this is max player	
			#compute evaluation value of this move
			self.getAllEndPoints(int(move.split(",")[0]),int(move.split(",")[1]),state)
			value1 = self.finalEvalList[-1]
			self.valueList.append(value1)
			if (depth != self.depth):
				printVal = "Infinity"
				self.traverselog.write(pointMapped+","+str(depth)+","+printVal)
				self.traverselog.write("\n")

				if (player == "w"):
					self.player = "b"
				else:
					self.player = "w"

				self.minimax(state,self.player,depth,nextPos)
			else:
				printVal = str(sum(self.valueList))
				self.traverselog.write(pointMapped+","+str(depth)+","+printVal)
				self.traverselog.write("\n")
				state[mapx][mapy] = "*" #marking as visited
				depth = depth - 1
				self.traverselog.write(parentMapped+","+str(depth)+","+printVal)
				self.traverselog.write("\n")
				self.minimax(state,player,depth,parent)

		else:
			#means this is min player
			self.getAllEndPoints(int(move.split(",")[0]),int(move.split(",")[1]),state)
			value1 = self.finalEvalList[-1]
			self.valueList.append(value1)
			
			if (depth != self.depth):
				printVal = "-Infinity"
				self.traverselog.write(pointMapped+","+str(depth)+","+str(printVal))
				self.traverselog.write("\n")

				if (player == "w"):
					self.player = "b"
				else:
					self.player = "w"

				self.minimax(state,self.player,depth,nextPos)
			else:
				printVal = str(sum(self.valueList))
				self.traverselog.write(pointMapped+","+str(depth)+","+printVal)
				self.traverselog.write("\n")
				state[mapx][mapy] = "*" #marking as visited
				depth = depth - 1
				self.traverselog.write(parentMapped+","+str(depth)+","+printVal)
				self.minimax(state,player,depth,parent)

	def greedy(self,state,player):
		currentPositions = self.getCurrentPositions(state)
		for i in range(0,len(currentPositions)):
			value = currentPositions[i]
			pos = value.split(",")
			xpos = int(pos[0])
			ypos = int(pos[1])
			legalAvailableMoves = self.getAvailableLegalMoves(xpos,ypos,state)
			legalAvailableMoves = list(set(legalAvailableMoves))

		self.calculateBestMove(legalAvailableMoves,state)
		if (self.player == "w"):
			maxEval = max(self.finalEvalList)
		else:
			minEval = min(self.finalEvalList)

		#find indices of duplicate maxVals. This is for tie breaking
		positions = []
		if (self.player == "w"):
			for i in range(0,len(self.finalEvalList)):
				if (self.finalEvalList[i] == maxEval):
					positions.append(self.finalMovePositions[i])
		else:
			for i in range(0, len(self.finalEvalList)):
				if (self.finalEvalList[i] == minEval):
					positions.append(self.finalMovePositions[i])

		xpositions = []
		ypositions = []

		if (len(positions) == 1):
			for i in range(0,len(positions)):
				xpositions.append(int(positions[i].split(",")[0]))
				ypositions.append(int(positions[i].split(",")[1]))

			#compare the positions
			nextMovex = max(xpositions)
			nextMovey = min(ypositions)
		else:
			newList1 = []
			newList2 = []
			for i in range(0, len(positions)):
				ypositions.append(int(positions[i].split(",")[1]))

			nextMovey = min(ypositions)

			for i in range(0, len(positions)):
				if (int(positions[i].split(",")[1]) == nextMovey):
					newList1.append(positions[i])
			for i in range(0,len(newList1)):
				newList2.append(int(newList1[i].split(",")[0]))

			nextMovex = max(newList2)

		self.writeNextState(nextMovex,nextMovey,state)

def main():
	sys.setrecursionlimit(50000)
	g = Game()
	f = open(argv[1],"r")
	contents = f.read()
	f.close
	contents = contents.rstrip().split("\n")
	algorithm = contents[0]
	player = contents[1]

	if (player == "1"):
		currentPlayer = "b"
	else:
		currentPlayer = "w"

	player = currentPlayer
	g.player = player
	g.traverselog = open("traverse_log.txt", "a")
	g.algo = algorithm
	depth = contents[2]
	gridSize = contents[3]
	boardState = []

	g.gridSize = int(gridSize)

	for i in range(0,int(gridSize)):
		boardState.append([])
		for j in contents[i+4]:
			boardState[i].append(j)
	
	g.state = boardState
	g.depth = int(depth)
	move = "root"
	g.stateCopy = boardState
	if algorithm == "1":
		g.greedy(boardState,player)
	elif (algorithm == "2"):
		g.traverselog.write("Move"+","+"Depth"+","+"Value")
		g.traverselog.write("\n")
		g.minimax(boardState,player,0,move)

if __name__ == "__main__":
    main()
