import psutil


def sys_metrics():

    """
    This API will use the psutil python Framework
    Collect the system metrics like: Disk, Memory, CPU percentage
    Return the value as Dict for FAST API
    """
    cpu_percentage = psutil.cpu_percent(interval=1)
    disk_percentage = psutil.disk_usage("/").percent
    memory_percentage = psutil.virtual_memory().percent

    threshold = 10

    status = "Healthy" if cpu_percentage < 10 else "Service not Healthy"

    return {
            "CPU Percentage": cpu_percentage,
            "Disk Percentage": disk_percentage,
            "Memory Percentage": memory_percentage,
            "CPU Threshold": threshold,
            "Status": status
            }
