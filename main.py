from fastapi import Form
import pandas as pd
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import joblib

# Create FastAPI application
app = FastAPI()

# Load the trained pipeline
model = joblib.load("model.joblib")

# Configure templates
templates = Jinja2Templates(directory="templates")

# Configure static files
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html"
    )

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html"
    )

@app.get("/predict", response_class=HTMLResponse)
def predict_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="predict.html",
        context={"prediction": None}
    )


@app.post("/predict", response_class=HTMLResponse)
def predict(
    request: Request,

    lagging_reactive: float = Form(...),
    leading_reactive: float = Form(...),
    co2: float = Form(...),
    lagging_pf: float = Form(...),
    leading_pf: float = Form(...),

    nsm: int = Form(...),
    hour: int = Form(...),
    month: int = Form(...),

    power_factor_ratio: float = Form(...),
    high_load: int = Form(...),

    week_status: str = Form(...),
    day_of_week: str = Form(...),
    load_type: str = Form(...),
    day_type: str = Form(...)
):

    data = {

        "Lagging_Current_Reactive.Power_kVarh": lagging_reactive,
        "Leading_Current_Reactive_Power_kVarh": leading_reactive,
        "CO2(tCO2)": co2,
        "Lagging_Current_Power_Factor": lagging_pf,
        "Leading_Current_Power_Factor": leading_pf,
        "NSM": nsm,
        "Hour": hour,
        "Month": month,
        "Power_Factor_Ratio": power_factor_ratio,
        "High_Load": high_load,

        "WeekStatus_Weekend": 0,

        "Day_of_week_Monday": 0,
        "Day_of_week_Saturday": 0,
        "Day_of_week_Sunday": 0,
        "Day_of_week_Thursday": 0,
        "Day_of_week_Tuesday": 0,
        "Day_of_week_Wednesday": 0,

        "Load_Type_Maximum_Load": 0,
        "Load_Type_Medium_Load": 0,

        "Day_Name_Monday": 0,
        "Day_Name_Saturday": 0,
        "Day_Name_Sunday": 0,
        "Day_Name_Thursday": 0,
        "Day_Name_Tuesday": 0,
        "Day_Name_Wednesday": 0,

        "Day_Type_Weekend": 0
    }

    # Week Status
    if week_status == "Weekend":
        data["WeekStatus_Weekend"] = 1

    # Day of Week
    if day_of_week == "Monday":
        data["Day_of_week_Monday"] = 1
        data["Day_Name_Monday"] = 1

    elif day_of_week == "Tuesday":
        data["Day_of_week_Tuesday"] = 1
        data["Day_Name_Tuesday"] = 1

    elif day_of_week == "Wednesday":
        data["Day_of_week_Wednesday"] = 1
        data["Day_Name_Wednesday"] = 1

    elif day_of_week == "Thursday":
        data["Day_of_week_Thursday"] = 1
        data["Day_Name_Thursday"] = 1

    elif day_of_week == "Saturday":
        data["Day_of_week_Saturday"] = 1
        data["Day_Name_Saturday"] = 1

    elif day_of_week == "Sunday":
        data["Day_of_week_Sunday"] = 1
        data["Day_Name_Sunday"] = 1

    # Friday is the reference category, so all remain 0.

    # Load Type
    if load_type == "Medium Load":
        data["Load_Type_Medium_Load"] = 1

    elif load_type == "Maximum Load":
        data["Load_Type_Maximum_Load"] = 1

    # Light Load is the reference category.

    # Day Type
    if day_type == "Weekend":
        data["Day_Type_Weekend"] = 1

    input_df = pd.DataFrame([data])

    prediction = model.predict(input_df)[0]

    return templates.TemplateResponse(
        request=request,
        name="predict.html",
        context={
            "prediction": round(float(prediction), 2)
        }
    )