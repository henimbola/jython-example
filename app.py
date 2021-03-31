from javax.swing import JFrame, JLabel, JButton, JTextField
from java.awt import Dimension

frame = JFrame("Hello")
frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
frame.setLocation(100,100)
frame.setSize(300,200)
frame.setLayout(None)

def add(event):
   print "add"
   ttl = int(txt1.getText())+int(txt2.getText())
   txt3.setText(str(ttl))

lbl1 = JLabel("Phy")
lbl1.setBounds(60,20,40,20)
txt1 = JTextField(10)
txt1.setBounds(120,20,60,20)
lbl2 = JLabel("Maths")
lbl2.setBounds(60,50,40,20)
txt2 = JTextField(10)
txt2.setBounds(120, 50, 60,20)
btn = JButton("Add", actionPerformed = add)
btn.setBounds(60,80,60,20)
lbl3 = JLabel("Total")
lbl3.setBounds(60,110,40,20)
txt3 = JTextField(10)
txt3.setBounds(120, 110, 60,20)

frame.add(lbl1)
frame.add(txt1)
frame.add(lbl2)
frame.add(txt2)
frame.add(btn)
frame.add(lbl3)
frame.add(txt3)
frame.setVisible(True)