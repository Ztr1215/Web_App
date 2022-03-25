import xml.etree.ElementTree as ET
import os
from xml.etree.ElementTree import ElementTree
from WOF.models import *

def writeCourseToXML(university_slug, courseSlug : str, courseDescription : str):
	WORK_DIR = os.getcwd()
	tree = ET.parse(os.path.join(WORK_DIR, "static", "xml", "uni_course_info.xml"))
	rootElement = tree.getroot()
	universities = list(rootElement)
	for uni in universities:
		if (uni.attrib.get('id') == university_slug):
			university_element = uni
			break
		university = University.objects.all()[0]
	print(university_element)
	course_element = ET.SubElement(university_element, "course")
	course_element.set('id', courseSlug)
	course_element.text = courseDescription
	tree.write(os.path.join(WORK_DIR, "static", "xml", "uni_course_info.xml"))
	return

def writeUniversityToXML(university_slug : str):
	WORK_DIR = os.getcwd()
	tree = ET.parse(os.path.join(WORK_DIR, "static", "xml", "uni_course_info.xml"))
	rootElement = tree.getroot()
	university_element = ET.SubElement(rootElement, "university")
	university_element.set('id', university_slug)
	tree.write(os.path.join(WORK_DIR, "static", "xml", "uni_course_info.xml"))
