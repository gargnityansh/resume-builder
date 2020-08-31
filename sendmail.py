import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
   

def sendMail(reciever_address, resource_name)
	fromaddr = "resumebuildersgsits@gmail.com"
	toaddr = reciever_address
	try:   
		msg = MIMEMultipart() 
		  
		msg['From'] = fromaddr 
		msg['To'] = toaddr 
		msg['Subject'] = "Resume Generated Through Resume Builder Sgsits"
		   
		body = "Below is the attach file of your Resume. Hope we will meet again"
		   
		msg.attach(MIMEText(body, 'plain')) 
		  
		filename = resource_name
		attachment = open(filename, "rb") 
		  

		p = MIMEBase('application', 'octet-stream') 
		  
		p.set_payload((attachment).read()) 
		  
		encoders.encode_base64(p) 
		   
		p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
		  
		msg.attach(p) 
		  
		s = smtplib.SMTP('smtp.gmail.com', 587) 
		s.starttls()
		s.login(fromaddr, "***********")
		text = msg.as_string() 
		s.sendmail(fromaddr, toaddr, text) 
		s.quit()
	
	except:
		print("Mail Not Send")

	return
