<p align="center">
<img src="AutoArea_Logo.png" width=300 height=300>
</p>

# AutoArea
AutoArea is area-annotator software for AutoCAD drawings. AutoArea is an AutoCAD automation tool that integrates AutoLISP and Python to automatically calculate, annotate, and manage area information in CAD drawings. It is designed to streamline repetitive drafting tasks and reduce manual errors by triggering area calculations and annotations during drawing events such as file save.

## Problem Statement:
Manual calculation and annotation of areas in AutoCAD drawings is time-consuming, error-prone, and inconsistent across projects. Existing workflows require repeated user intervention and often lead to outdated annotations when drawings are modified.

## System Architecture: 
### AutoCAD (AutoLISP)
Loads automation at startup (acaddoc.lsp)
<br>
Listens to drawing events using reactors
<br>
Invokes Python scripts via startapp

### Python Layer
Extracts entity and geometry data
<br>
Computes areas accurately
<br>
Generates annotations and metadata

## Tools & Technologies
AutoLISP – AutoCAD automation and event reactors
<br>
Python – Geometry processing and logic
<br>
AutoCAD – Target CAD platform

## Applications: 
AutoArea finds applicability in the design and plan of architectural drawings, site-planning, interior design. Manual workflows in such cases are error-prone and slow.
