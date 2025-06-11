package iagoav.iewiki;

import static androidx.core.content.ContextCompat.startActivity;

import android.content.Context;
import android.content.Intent;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.squareup.picasso.Picasso;

public class RecyclerViewHolder extends RecyclerView.ViewHolder {

    private TextView textView;
    private ImageView imageView;

    public RecyclerViewHolder(@NonNull View itemView) {
        super(itemView);
        textView = itemView.findViewById(R.id.nombreE);
        imageView = itemView.findViewById(R.id.imageTeam);
        textView = itemView.findViewById(R.id.entrenador);
    }

    public void showData(TeamDTO teamDTO) {
        this.textView.setText(teamDTO.getName());
        this.textView.setText(teamDTO.getCoach());
        String imageUrl = "http://10.0.2.2:8000/" + teamDTO.getImage();
        Picasso.get().load(imageUrl).into(imageView);

        itemView.setOnClickListener(v -> {
            Context context = itemView.getContext();
            Intent intent = new Intent(context, JugadoresActivity.class);
            intent.putExtra("name", teamDTO.getName());
            intent.putExtra("coach", teamDTO.getCoach());
            intent.putExtra("id", teamDTO.getId());
            intent.putExtra("image", teamDTO.getImage());


            context.startActivity(intent);
        });
    }


}
