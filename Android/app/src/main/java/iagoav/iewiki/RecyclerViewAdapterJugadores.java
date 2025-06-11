package iagoav.iewiki;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class RecyclerViewAdapterJugadores extends  RecyclerView.Adapter<RecyclerViewHolderJugadores>{

    private List<JugadoresDTO> jugadoresList;

    public RecyclerViewAdapterJugadores(List<JugadoresDTO> jugadoresList){
        this.jugadoresList = jugadoresList;
    }


    @NonNull
    @Override
    public RecyclerViewHolderJugadores onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        LayoutInflater inflater = LayoutInflater.from(parent.getContext());
        View itemjugador = inflater.inflate(R.layout.item_jugador, parent, false);
        return new RecyclerViewHolderJugadores(itemjugador);
    }

    @Override
    public void onBindViewHolder(@NonNull RecyclerViewHolderJugadores holder, int position) {
        JugadoresDTO jugadores = jugadoresList.get(position);
        holder.showData(jugadores);
    }

    @Override
    public int getItemCount() {
        return jugadoresList.size();
    }


}
