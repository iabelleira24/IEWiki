package iagoav.iewiki;


import android.content.Context;
import android.content.Intent;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.squareup.picasso.Picasso;

public class RecyclerViewHolderCatalogo extends RecyclerView.ViewHolder  {

    private TextView textView3;
    private ImageView imageView3;


    public RecyclerViewHolderCatalogo(@NonNull View itemView) {
        super(itemView);
        textView3 = itemView.findViewById(R.id.nombreJ);
        imageView3 = itemView.findViewById(R.id.imagenJ);

    }

    public void showData(JugadoresCatalogoDTO jugadoresCatalogoDTO) {
        textView3.setText(jugadoresCatalogoDTO.getNameJ());


        String imageUrl = "http://10.0.2.2:8000/" + jugadoresCatalogoDTO.getImageJ();
        Picasso.get().load(imageUrl).into(imageView3);

        itemView.setOnClickListener(v -> {
            Context context = itemView.getContext();
            Intent intent = new Intent(context, JugadorDetalle.class);
            intent.putExtra("id", jugadoresCatalogoDTO.getId());
            context.startActivity(intent);
        });
    }
}
