<p align="center"><img src="images/AutoArea_Logo.png" alt="AutoArea Logo" width="200" height="300">
</p>

# AutoLISP:
It is a programming language directly built into AutoCAD. It is used to automate drawing tasks, create custom commands.
<br>
It is built into AutoCAD directly.
<br>
It interacts directly with DWG objects.
<br>
It works well with python.
<br>
Example: 
```bash
(startapp "python.exe" "yourscript.py")
```
It is used for automation: you can trigger scripts on drawing save, drawing open, object modification, etc.

## Rules/syntax:
1. Everything is inside paranthesis
```bash
(function arg1 arg2 arg3 ...)
```
Thus, it follows pref-fix notation. (operator before operands)

2. To assign variables: 
```bash
(setq a 10)
(setq b 20)
(+ a b)         ; 30
```

3. Defining functions: 
```bash
(defun add2 (x y)
  (+ x y)
)
```
 To define an AutoCAD command: 
 ```bash
 (defun c:hello ()
  (princ "Hello!")
)
```
4. Comments: 
Anything after ; is a comment.

5. Lists: 

```bash
'(list items)
```

A point in cartesian plane is also a list.

6. Calling an AutoCAD command: 
```bash
(command "LINE" '(0 0) '(50 50) "")
(command "CIRCLE" '(10 10) 20)
(command "TEXT" "0,0" 100 "Hello")
```
## Reactors: 

Reactors are event-listeners in AutoLISP. They react automatically when something happens in the document.

| Reactor Type            | Trigger Example                      |
| ----------------------- | ------------------------------------ |
| **VLR-DWG-REACTOR**     | Save, Open, Close, Begin/End Command |
| **VLR-OBJECT-REACTOR**  | When a specific object changes       |
| **VLR-EDIT-REACTOR**    | User modifying content               |
| **VLR-COMMAND-REACTOR** | Start or end of any AutoCAD command  |
| **VLR-SYSTEM-REACTOR**  | System events like quitting AutoCAD  |

Syntax of reactors: 
```bash
(vlr-dwg-reactor
  owner-object
  '((event-name . callback-function))
)
```
(for drawing reactors.)

1. The owner-object: It determines what <b>object</b> the reactor is associated with. The reactor fires when that <p>particular</b> object changes. 
2. (event.callback): <br>
Event: which AutoCAD listens for.
<br>
Callback: The function to run when the event happens.
<br>

| Event Name                 | Meaning                      |
| -------------------------- | ---------------------------- |
| `:vlr-saveComplete`        | Fires after drawing is saved |
| `:vlr-beginSave`           | Fires when save begins       |
| `:vlr-commandEnded`        | Fires when any command ends  |
| `:vlr-commandWillStart`    | Fires when command starts    |
| `:vlr-databaseConstructed` | When drawing opens           |
| `:vlr-beginClose`          | When drawing starts closing  |

The callback function must have the format: 
```bash
(defun OnSave (reactor-object reactor-data)
  ;; your code here
)
```
## How to run the code: 
To run the code everytime a drawing is created, save the lisp code into acaddoc.lsp.

Sample directory layout: 
D:\AutoCAD_Automation\
│
├── lisp\
│   ├── mysaveautomation.lsp   ← reactor here
│   └── acaddoc.lsp            ← loads the automation
│
└── python\
    ├── area_calc.py
    ├── annotate_dwg.py

