from reportlab.pdfgen import canvas

class Invoice():
    def __init__(self, KID, kroner, ore, kontonr, org):
        self.KID = KID
        self.kroner = kroner
        self.ore = ore
        self.kontonr = kontonr
        self.org = org
        
    def __call__(self):
        c = canvas.Canvas(self.KID + ".pdf")
        c.setPageSize((720, 1018))
        c.drawInlineImage("faktura.jpg", 0, 0)
        c.drawString(50,33, self.KID)
        c.drawString(280,33, self.kroner + ",-")
        c.drawString(280,320, self.kroner + ",-")
        if len(self.ore) == 1:
            c.drawString(402,33, "0" + self.ore)
        else:
            c.drawString(402,33, self.ore)
            
        c.drawString(450,33, self.kontonr[0:5] + " " + self.kontonr[5:7] + " " + self.kontonr[7:])
        c.drawString(50,500, self.org)
        
            

        return c.save()


