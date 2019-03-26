#MenuTitle: Calligraphic Guidelines
# -*- coding: utf-8 -*-
__doc__="""
Create Calligraphic Guidelines.
"""

#-------------------
# Global Variables  
#-------------------

Font = Glyphs.font
FontMaster = Font.selectedFontMaster
selectedLayers = Font.selectedLayers

#-------------------
# Local Variables
#-------------------

GuideLinePos = [-566, 0, 1132, 1698]

#-------------------
# Definitions
#-------------------

def increaseSideBearing(increaseSBFactor):
	for thisLayer in selectedLayers:
 		thisGlyph = thisLayer.parent 
   		thisLayer.LSB += increaseSBFactor * thisLayer.LSB;
 		thisLayer.RSB += increaseSBFactor * thisLayer.RSB;

def drawRect(myBottomLeft, myTopRight):
	myRect = GSPath()
	myCoordinates = [
		[ myBottomLeft[0], myBottomLeft[1] ],
		[ myTopRight[0], myBottomLeft[1] ],
		[ myTopRight[0], myTopRight[1] ],
		[ myBottomLeft[0], myTopRight[1] ]
	]
	
	for thisPoint in myCoordinates:
		newNode = GSNode()
		newNode.type = GSLINE
		newNode.position = ( thisPoint[0], thisPoint[1] )
		myRect.nodes.append( newNode )
	
	myRect.closed = True
	return myRect
	
def process(thisLayer):
	for i in GuideLinePos:
		bottomLeft = ( 0, i-8 )
		topRight = ( thisLayer.width, i+8 )
		layerRect = drawRect( bottomLeft, topRight )
		thisLayer.paths.append( layerRect )

def process2(thisLayer):
	bottomLeft = ( 50.0, 0.0 )
	topRight = ( thisLayer.width - 50.0, 600.0 )
	layerRect = drawRect( bottomLeft, topRight )
	thisLayer.paths.append( layerRect )
		

#-------------------
# Commands
#-------------------

#increaseSideBearing(0.3)

for thisLayer in selectedLayers:
	thisGlyph = thisLayer.parent
	process(thisLayer)
