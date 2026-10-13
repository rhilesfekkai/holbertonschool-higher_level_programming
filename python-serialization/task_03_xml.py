#!/usr/bin/env python3
"""Serialize and deserialize dictionaries using XML."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to an XML file."""
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, str(key))
        child.text = str(value)

    tree = ET.ElementTree(root)
    ET.indent(tree, space="    ")
    tree.write(filename, encoding="unicode", xml_declaration=False)


def deserialize_from_xml(filename):
    """Deserialize an XML file into a dictionary."""
    tree = ET.parse(filename)
    root = tree.getroot()

    return {
        child.tag: child.text if child.text is not None else ""
        for child in root
    }
