all : primecards.pdf primecards-a4.pdf primecards-screen.pdf \
	snakeboard.pdf boardsquares.pdf \
	primes-game.pdf

EPS := resources/2.eps

primecards.pdf : primecards.ps common.ps $(EPS)
	gs --permit-file-read=./ --permit-file-read=resources/ -sDEVICE=pdfwrite -sOutputFile=primecards.pdf -dBATCH -dNOPAUSE primecards.ps

primecards-a4.pdf : primecards.ps common.ps $(EPS)
	gs --permit-file-read=./ --permit-file-read=resources/ -sDEVICE=pdfwrite -sOutputFile=primecards-a4.pdf -dBATCH -dNOPAUSE -dNinePerPage -dCardGrid primecards.ps

primecards-screen.pdf : primecards.ps common.ps $(EPS)
	gs --permit-file-read=./ --permit-file-read=resources/ -sDEVICE=pdfwrite -sOutputFile=primecards-screen.pdf -dBATCH -dNOPAUSE -dCardClip -sBleed=0.5 primecards.ps

snakeboard.pdf : snakeboard.ps common.ps $(EPS)
	gs --permit-file-read=./ --permit-file-read=resources/ -sDEVICE=pdfwrite -sOutputFile=snakeboard.pdf -dBATCH -dNOPAUSE snakeboard.ps

boardsquares.pdf : snakeboard.ps common.ps $(EPS)
	gs --permit-file-read=./ --permit-file-read=resources/ -sDEVICE=pdfwrite -sOutputFile=boardsquares.pdf -dBATCH -dNOPAUSE -dBoardSquares snakeboard.ps

primes-game.pdf : primes-game.tex boardsquares.pdf primecards-screen.pdf
	lualatex primes-game.tex

# List of all SVG files
SVGS := $(wildcard resources/*.svg)

# generate all EPS files
$(EPS): $(SVGS)
	cd resources && python3 makeeps.py
