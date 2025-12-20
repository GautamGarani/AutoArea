<p align="center">
  <img src="AutoArea_Logo.png" width=300 height=300 style="border: 5px solid blue;">
</p>

# 🧩 AutoArea
 **AutoArea** is an area-annotator software for AutoCAD drawings. It is an AutoCAD automation tool that integrates **AutoLISP** and **Python** to automatically calculate, annotate, and manage area information in CAD drawings.

It streamlines repetitive drafting tasks and reduces manual errors by triggering area calculations and annotations during drawing events such as **file save**.  
AutoArea was designed as a small college project.


## Problem Statement
Manual calculation and annotation of areas in AutoCAD drawings is **time-consuming**, **error-prone**, and **inconsistent** across projects. Existing workflows require repeated user intervention and often lead to **outdated annotations** when drawings are modified.


## 🏗️ System Architecture
### AutoCAD (AutoLISP)
- Loads automation at startup (`acaddoc.lsp`)
- Listens to drawing events using reactors
- Invokes Python scripts via `startapp`
  
### Python Layer
- Extracts entity and geometry dat
- Computes areas accurately
- Generates annotations and metadata

## 🛠️ Tools & Technologies
- AutoLISP – AutoCAD automation and event reactors
- Python – Geometry processing and logic
- AutoCAD – Target CAD platform

## 🏢 Applications
AutoArea is applicable in:
- Architectural drawings  
- Site planning  
- Interior design  

Manual workflows in such cases are slow and error-prone, making automation highly beneficial.

## 👥 Contributors
- **Gautam Garani** | https://github.com/GautamGarani  
- **Dhaksh** | https://github.com/Dhaksh-1106

