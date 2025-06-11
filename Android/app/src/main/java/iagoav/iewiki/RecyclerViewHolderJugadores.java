package iagoav.iewiki;

import android.content.Context;
import android.content.Intent;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.squareup.picasso.Picasso;

public class RecyclerViewHolderJugadores extends RecyclerView.ViewHolder {
    private TextView textView2;
    private ImageView imageView2;
    private TextView textView3;

    public RecyclerViewHolderJugadores(@NonNull View itemView) {
        super(itemView);
        textView2 = itemView.findViewById(R.id.nombreJ);
        imageView2 = itemView.findViewById(R.id.imagenJ);
        textView3 = itemView.findViewById(R.id.posicionJ);
    }

    public void showData(JugadoresDTO jugadoresDTO) {
        textView2.setText(jugadoresDTO.getNameJ());
        textView3.setText(jugadoresDTO.getPositionJ());


        String imageUrl = "http://10.0.2.2:8000/" + jugadoresDTO.getImageJ();
        Picasso.get().load(imageUrl).into(imageView2);

        itemView.setOnClickListener(v -> {
            Context context = itemView.getContext();
            Intent intent = new Intent(context, JugadorDetalle.class);
            intent.putExtra("id", jugadoresDTO.getId());
            context.startActivity(intent);
        });
    }
}
