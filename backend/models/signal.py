"""Signal Models"""
from pydantic import BaseModel
from typing import List
from datetime import datetime

class StrategySignal(BaseModel):
    strategy: str
    confidence: float

class Signal(BaseModel):
    symbol: str
    timeframe: str
    signal_type: str
    entry_price: float
    take_profit: float
    stop_loss: float
    signal_strength: float
    buy_signals: List[StrategySignal] = []
    sell_signals: List[StrategySignal] = []
    total_strategies: int
    agreement_percentage: float
    created_at: datetime = datetime.now()

class SignalResponse(BaseModel):
    symbol: str
    timeframe: str
    signal: Signal
    timestamp: datetime
