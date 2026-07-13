# app/core/logger.py
import logging
import sys

def get_logger(module_name: str):
    logger = logging.getLogger(module_name)
    
    # Mencegah duplikasi log jika logger dipanggil berkali-kali
    if not logger.hasHandlers():
        logger.setLevel(logging.INFO) # Default level: INFO
        
        # Format: Waktu - Nama File - Level - Pesan
        formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        
        # Arahkan log ke terminal (stdout)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        
        logger.addHandler(console_handler)
        
    return logger