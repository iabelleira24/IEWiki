package iagoav.iewiki;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class RecyclerViewAdapterCatalogo extends  RecyclerView.Adapter<RecyclerViewHolderCatalogo> {
    private List<JugadoresCatalogoDTO> jugadoresList2;

    public RecyclerViewAdapterCatalogo(List<JugadoresCatalogoDTO> jugadoresList2) {
        this.jugadoresList2 = jugadoresList2;
    }

    @NonNull
    @Override
    public RecyclerViewHolderCatalogo onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        LayoutInflater inflater = LayoutInflater.from(parent.getContext());
        View itemjugadorcatalogo = inflater.inflate(R.layout.item_jugadorcatalogo, parent, false);
        return new RecyclerViewHolderCatalogo(itemjugadorcatalogo);
    }

    @Override
    public void onBindViewHolder(@NonNull RecyclerViewHolderCatalogo holder, int position) {
        JugadoresCatalogoDTO jugadoresC = jugadoresList2.get(position);
        holder.showData(jugadoresC);
    }


    @Override
    public int getItemCount() {
        return jugadoresList2.size();
    }



}








