from typing import List
import streamlit as st
from models import Item
import dao as db

class ItemController:
    @staticmethod
    def obter_todos_os_itens() -> List[Item]:
        return db.listar_todos()

    @staticmethod
    def criar_item(nome: str, descricao: str, quantidade: int) -> None:
        if len(nome) < 5:
            return {"error_id": 0, "description": "O nome deve conter mais de 5 caracteres."}
        try:
            quantidade = int(quantidade)
        except:
            return {"error_id": 1, "description": "Você deve informar uma quantidade numérica."}
        if quantidade <= 0:
            return {"error_id": 2, "description": "Você deve ter pelo menos um item disponível."}

        new_item = Item(id=0, nome=nome, descricao=descricao, quantidade=quantidade)
        
        db.adicionar(new_item)