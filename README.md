# ai-detyra2-Astar

## Qka eshte A*

A* është një algoritëm për gjetjen e shtigjeve. Është një lloj algoritmi i kërkimit më të mirë të parë që përdor një funksion heuristik për të përcaktuar rendin në të cilin kërkohet grafiku. 
Algoritmi A* përdoret gjerësisht në videolojëra, dizajn me kompjuter, robotikë dhe fusha të tjera.

## Qka eshte nje funksion heuristik

Funksioni heuristik, i njohur gjithashtu si "kostoja e vlerësuar" për të arritur qëllimin, përdoret për të përcaktuar koston totale të një shtegu, që është shuma e kostos së shtegut deri tani dhe një vlerësim i kostos së shtegut të mbetur. drejt qëllimit. Algoritmi zgjedh në mënyrë të përsëritur nyjen me koston totale më të ulët të vlerësuar për t'u zgjeruar më pas, dhe ndalon kur arrin nyjen e qëllimit ose kur përcakton se një rrugë drejt qëllimit nuk ekziston.

Funksioni heuristik i perdorur ne kete punim eshte "Manhattan Distancen" ku distanca llogaritet si diferencë absolute në koordinatat x plus diferencën absolute në koordinatat y.

## Ekzekutimi

  ```shell
  python3 aStar.py
  ```
