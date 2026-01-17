; program to automatically run python AutoArea script on save
;------------------------------------------------------------

(defun AutoArea:run_py (reactor params)
  (startapp "\"the-path-to-python.exe\""
	    "\"the-path-to-main.py\""
  )
)


; Reactor should NOT run the python program multiple times:
; Reactor is created if it does not exist, and stored into AutoArea_SaveReactor so that it is NOT created again and again

(if (not AutoArea_SaveReactor)
  (setq AutoArea_SaveReactor
	 (vlr-dwg-reactor
	   ""
	   '((:vlr-saveComplete . AutoArea:run_py))
	 )
  )
)

(princ)


 
