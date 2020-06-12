import ROOT
h=ROOT.TH1F("gauss","Example histogram",100,-4,4)
h.FillRandom("gaus")
c=ROOT.TCanvas("myCanvasName","The Canas Title",800,600)
h.Draw()
c.Draw()
