from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/singaporeschools' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)

class General_Details(db.Model):
    __tablename__ = 'generaldetails'
    School_Code = db.Column(db.Integer, primary_key=True)
    School_Name = db.Column(db.String(100), nullable=False)
    School_Region = db.Column(db.String(50), nullable=False)
    School_Address = db.Column(db.String(150), nullable=False)
    School_Postal_Code = db.Column(db.String(50), nullable=False)
    School_Mode = db.Column(db.String(50), nullable=False)
    School_Nature = db.Column(db.String(50), nullable=False)
    School_Type = db.Column(db.String(50), nullable=False)
    School_Number = db.Column(db.String(50), nullable=False)
    School_Email = db.Column(db.String(50), nullable=False)
    School_Website = db.Column(db.String(150), nullable=False)
    School_Image_Source = db.Column(db.String(200), nullable=False)

    



class PSLE_Scores(db.Model):
    __tablename__ = 'PSLE_Score_Details'
    School_Code = db.Column(db.Integer, primary_key=True)
    IP_Affiliation = db.Column(db.String(50), nullable=False)
    IP_NonAffiliation = db.Column(db.String(50), nullable=False)
    Express_Affiliation = db.Column(db.String(50), nullable=False)
    Express_NonAffiliation = db.Column(db.String(50), nullable=False)
    NA_Affiliation = db.Column(db.String(50), nullable=False)
    NA_NonAffiliation = db.Column(db.String(50), nullable=False)
    NT_Affiliation = db.Column(db.String(50), nullable=False)
    NT_NONAffiliation = db.Column(db.String(50), nullable=False)

class Subjects(db.Model):
    __tablename__ = 'Subjects_Offered'
    School_Code = db.Column(db.Integer, primary_key=True)
    Subject_Offered = db.Column(db.String(50), primary_key=True)

class DSA(db.Model):
    __tablename__ = 'dsa_opportunities'
    School_Code = db.Column(db.Integer, primary_key=True)
    DSA_CCA = db.Column(db.String(100), primary_key=True)

class CCA(db.Model):
    __tablename__ = 'cca_offered'
    School_Code = db.Column(db.Integer, primary_key=True)
    CCA_Offered = db.Column(db.String(100), primary_key=True)

class Special_Education(db.Model):
    __tablename__ = 'special_ed_support'
    School_Code = db.Column(db.Integer, primary_key=True)
    Special_Education_Support = db.Column(db.String(100), primary_key=True)

class Electives(db.Model):
    __tablename__ = 'electives'
    School_Code = db.Column(db.Integer, primary_key=True)
    Electives_Name = db.Column(db.String(100), primary_key=True)
    Elective_SubHeader = db.Column(db.String(100), nullable=False)
    Elective_Description = db.Column(db.String(100), primary_key=True)

class Affiliations(db.Model):
    __tablename__ = 'affiliations'
    School_Code = db.Column(db.Integer, primary_key=True)
    Affiliated_School = db.Column(db.String(100), primary_key=True)


@app.route("/details")
def get_all():
    all_schools = General_Details.query.all()
    if len(all_schools):
        school_data = []
        for school in all_schools:
            school_data.append({
                "School_Code": school.School_Code,
                "School_Name": school.School_Name,
                "School_Region": school.School_Region,
                "School_Address": school.School_Address,
                "School_Postal_Code": school.School_Postal_Code,
                "School_Mode": school.School_Mode,
                "School_Nature": school.School_Nature,
                "School_Type": school.School_Type,
                "School_Number": school.School_Number,
                "School_Email": school.School_Email,
                "School_Website": school.School_Website,
                "School_Image_Source": school.School_Image_Source
            })
        return jsonify(school_data)
    else:
        return jsonify(
            {
                "code": 404,
                "message": "There are no schools."
            }
        ), 404



if __name__ == '__main__':
    app.run(debug=True, port=5000)