function showReport(reportNumber) {
    // Hide all reports
    document.querySelectorAll('.report').forEach(report => {
        report.classList.add('hidden');
    });

    // Show the selected report
    document.getElementById(`report-${reportNumber}`).classList.remove('hidden');
}