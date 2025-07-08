class ExercicioBase {
    selecionarAleatorio(grupo) {
        const lista = this.exercicios[grupo];
        if (!lista || lista.length === 0) return null;
        const idx = Math.floor(Math.random() * lista.length);
        return lista[idx];
    }
}