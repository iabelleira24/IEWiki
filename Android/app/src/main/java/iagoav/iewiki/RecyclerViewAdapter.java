package iagoav.iewiki;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class RecyclerViewAdapter extends RecyclerView.Adapter<RecyclerViewHolder> {

    private List<TeamDTO> teamList;

    public RecyclerViewAdapter(List<TeamDTO> teamList) {
        this.teamList = teamList;
    }

    @NonNull
    @Override
    public RecyclerViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        LayoutInflater inflater = LayoutInflater.from(parent.getContext());
        View cellView = inflater.inflate(R.layout.recycler_view_cell, parent, false);
        return new RecyclerViewHolder(cellView);
    }

    @Override
    public void onBindViewHolder(@NonNull RecyclerViewHolder holder, int position) {
        TeamDTO team = teamList.get(position);
        holder.showData(team);
    }

    @Override
    public int getItemCount() {
        return teamList.size();
    }
}
