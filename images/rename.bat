for /R %location% %%A in (*.png) do call :repl "%%A"
goto :eof 

:repl
set "_fn=%~nx1"
ren %1 "%_fn: =_%"