""" BZFlag.UI.Drawable.Teleporter

Classes for drawing the teleporters in the world
"""
#
# Python BZFlag Protocol Package
# Copyright (C) 2003 Micah Dowty <micahjd@users.sourceforge.net>
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2.1 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
from DisplayList import *
from OpenGL.GL import *


class TeleporterField(DisplayList):
    def drawToList(self, center, angle, size):
        self.center = center
        self.angle = angle
        self.size = size
        self.blended = True
        glPushMatrix()
        glTranslatef(*self.center)
        glRotatef(self.angle, 0.0, 0.0, 1.0)
        glColor4f(0.0, 0.0, 0.0, 0.3)
        glDepthMask(0)
        glBegin(GL_QUADS)
        # X+ side
        glNormal3f(1, 0, 0)
        glVertex3f(self.size[0] / 2, self.size[1], 0)
        glVertex3f(self.size[0] / 2, self.size[1], self.size[2])
        glVertex3f(self.size[0] / 2, -self.size[1], self.size[2])
        glVertex3f(self.size[0] / 2, -self.size[1], 0)
        # X- side
        glNormal3f(-1, 0, 0)
        glVertex3f(-self.size[0] / 2, -self.size[1], 0)
        glVertex3f(-self.size[0] / 2, -self.size[1], self.size[2])
        glVertex3f(-self.size[0] / 2, self.size[1], self.size[2])
        glVertex3f(-self.size[0] / 2, self.size[1], 0)
        glEnd()
        glDepthMask(1)
        glColor3f(1.0, 1.0, 1.0)
        glPopMatrix()
	

class TeleporterBorder(DisplayList):
    textureName = 'caution.png'
    def drawToList(self, center, angle, size, border):
        self.center = center
        self.angle = angle
        self.size = size
        self.border = border
        glPushMatrix()
        glTranslatef(*self.center)
        glRotatef(self.angle, 0.0, 0.0, 1.0)
        glBegin(GL_TRIANGLE_STRIP)
        glNormal3f(-1, 0, 0)
        glTexCoord2f(0, 0)
        glVertex3f(-self.border / 2, self.size[1] + self.border, 0)
        glTexCoord2f(self.border, 0)
        glVertex3f(-self.border / 2, self.size[1], 0)
        glTexCoord2f(0, self.size[2] + self.border)
        glVertex3f(-self.border / 2, self.size[1] + self.border, self.size[2] + self.border)
        glTexCoord2f(self.border, self.size[2])
        glVertex3f(-self.border / 2, self.size[1], self.size[2])
        glTexCoord2f(2 * self.border + 2 * self.size[1], self.size[2] + self.border)
        glVertex3f(-self.border / 2, -self.size[1] - self.border, self.size[2] + self.border)
        glTexCoord2f(self.border + 2 * self.size[1], self.size[2])
        glVertex3f(-self.border / 2, -self.size[1], self.size[2])
        glTexCoord2f(2 * self.border + 2 * self.size[1], 0)
        glVertex3f(-self.border / 2, -self.size[1] - self.border, 0)
        glTexCoord2f(self.border + 2 * self.size[1], 0)
        glVertex3f(-self.border / 2, -self.size[1], 0)
        glEnd()
        glFrontFace(GL_CW)
        glBegin(GL_TRIANGLE_STRIP)
        glNormal3f(1, 0, 0)
        glTexCoord2f(0, 0)
        glVertex3f(self.border / 2, self.size[1] + self.border, 0)
        glTexCoord2f(self.border, 0)
        glVertex3f(self.border / 2, self.size[1], 0)
        glTexCoord2f(0, self.size[2] + border)
        glVertex3f(self.border / 2, self.size[1] + self.border, self.size[2] + self.border)
        glTexCoord2f(self.border, self.size[2])
        glVertex3f(self.border / 2, self.size[1], self.size[2])
        glTexCoord2f(2 * self.border + 2 * self.size[1], self.size[2] + self.border)
        glVertex3f(self.border / 2, -self.size[1] - self.border, self.size[2] + self.border)
        glTexCoord2f(self.border + 2 * self.size[1], self.size[2])
        glVertex3f(self.border / 2, -self.size[1], self.size[2])
        glTexCoord2f(2 * self.border + 2 * self.size[1], 0)
        glVertex3f(self.border / 2, -self.size[1] - self.border, 0)
        glTexCoord2f(self.border + 2 * self.size[1], 0)
        glVertex3f(self.border / 2, -self.size[1], 0)
        glEnd()
        glFrontFace(GL_CCW)
        glBegin(GL_QUADS)
        # top
        glNormal3f(0.4, 0, 1)
        glTexCoord2f(0.4, 0.0001)
        glVertex3f(self.border / 2, -self.size[1] - self.border, self.size[2] + self.border)
        glTexCoord2f(2 * self.border + 2 * self.size[1] + 0.4, 0.0001)
        glVertex3f(self.border / 2, self.size[1] + self.border, self.size[2] + self.border)
        glTexCoord2f(2 * self.border + 2 * self.size[1] + 0.4, 0)
        glVertex3f(-self.border / 2, self.size[1] + self.border, self.size[2] + self.border)
        glTexCoord2f(0.4, 0)
        glVertex3f(-self.border / 2, -self.size[1] - self.border, self.size[2] + self.border)
        # underside of top
        glNormal3f(0, 0, -1)
        glTexCoord2f(0.4, 0)
        glVertex3f(-self.border / 2, -self.size[1] - self.border, self.size[2])
        glTexCoord2f(2 * self.border + 2 * self.size[1] + 0.4, 0)
        glVertex3f(-self.border / 2, self.size[1] + self.border, self.size[2])
        glTexCoord2f(2 * self.border + 2 * self.size[1] + 0.4, 0.0001)
        glVertex3f(self.border / 2, self.size[1] + self.border, self.size[2])
        glTexCoord2f(0.4, 0.0001)
        glVertex3f(self.border / 2, -self.size[1] - self.border, self.size[2])
        # Y+ outside
        glNormal3f(0, 1, 0)
        glTexCoord2f(self.border, 0)
        glVertex3f(-self.border / 2, self.size[1] + border, 0)
        glTexCoord2f(self.border, self.size[2] + border)
        glVertex3f(-self.border / 2, self.size[1] + self.border, self.size[2] + self.border)
        glTexCoord2f(0, self.size[2] + self.border)
        glVertex3f(self.border / 2, self.size[1] + self.border, self.size[2] + self.border)
        glTexCoord2f(0, 0)
        glVertex3f(self.border / 2, self.size[1] + self.border, 0)
        # Y+ inside
        glNormal3f(0, -1, 0)
        glTexCoord2f(0, 0)
        glVertex3f(self.border / 2, self.size[1], 0)
        glTexCoord2f(0, self.size[2])
        glVertex3f(self.border / 2, self.size[1], self.size[2])
        glTexCoord2f(self.border, self.size[2])
        glVertex3f(-self.border / 2, self.size[1], self.size[2])
        glTexCoord2f(self.border, 0)
        glVertex3f(-self.border / 2, self.size[1], 0);
        # Y- outside
        glNormal3f(0, 1, 0)
        glTexCoord2f(0, 0)
        glVertex3f(self.border / 2, -self.size[1] - self.border, 0)
        glTexCoord2f(0, self.size[2] + self.border)
        glVertex3f(self.border / 2, -self.size[1] - self.border, self.size[2] + self.border)
        glTexCoord2f(self.border, self.size[2] + self.border)
        glVertex3f(-self.border / 2, -self.size[1] - self.border, self.size[2] + self.border)
        glTexCoord2f(self.border, 0)
        glVertex3f(-self.border / 2, -self.size[1] - self.border, 0)
        # Y- inside
        glNormal3f(0, -1, 0)
        glTexCoord2f(self.border, 0)
        glVertex3f(-self.border / 2, -self.size[1], 0)
        glTexCoord2f(self.border, self.size[2])
        glVertex3f(-self.border / 2, -self.size[1], self.size[2])
        glTexCoord2f(0, self.size[2])
        glVertex3f(self.border / 2, -self.size[1], self.size[2])
        glTexCoord2f(0, 0)
        glVertex3f(self.border / 2, -self.size[1], 0)
        # Y+ leg bottom
        glNormal3f(0, 0, -1)
        glTexCoord2f(self.border, self.border)
        glVertex3f(self.border / 2, self.size[1] + self.border, 0)
        glTexCoord2f(0, self.border)
        glVertex3f(self.border / 2, self.size[1], 0)
        glTexCoord2f(0, 0)
        glVertex3f(-self.border / 2, self.size[1], 0)
        glTexCoord2f(self.border, 0)
        glVertex3f(-self.border / 2, self.size[1] + self.border, 0)
        # Y- leg bottom
        glNormal3f(0, 0, -1);
        glTexCoord2f(self.border, self.border);
        glVertex3f(-self.border / 2, -self.size[1] - self.border, 0);
        glTexCoord2f(self.border, 0);
        glVertex3f(-self.border / 2, -self.size[1], 0);
        glTexCoord2f(0, 0);
        glVertex3f(self.border / 2, -self.size[1], 0);
        glTexCoord2f(0, self.border);
        glVertex3f(self.border / 2, -self.size[1] - self.border, 0);
        glEnd()
        glPopMatrix()


### The End ###
