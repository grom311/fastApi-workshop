from fastapi import APIRouter, Depends, File, UploadFile
from fastapi.responses import StreamingResponse

from models.auth import User
from services.auth import get_current_user
from services.reports import ReportService

router = APIRouter(prefix='/reports')


@router.post('/import')
def import_csv(
    file: UploadFile = File(...),
    user: User = Depends(get_current_user),
    report_service: ReportService = Depends()
):
    report_service.import_csv(user.id, file.file)

@router.get('/export')
def export_csv(
    user: User = Depends(get_current_user),
    report_service: ReportService = Depends()
):
    report = report_service.export_csv(user.id)
    return StreamingResponse(
        report,
        media_type='text/csv',
        headers={
            'Content-Disposition': 'attachment; filename=report.csv'
        }
    )