package iagoav.iewiki.multipleView;

import android.content.Context;
import android.view.View;
import android.view.ViewGroup;
import android.widget.LinearLayout;

import androidx.constraintlayout.widget.ConstraintLayout;

public class MultipleView {
    private MultipleViewAdapter adapter;

    public void setAdapter(MultipleViewAdapter adapter) {
        this.adapter = adapter;
    }



    public void repintar(){
        for (int i = 1; i <= this.adapter.getItemCount(); i++){

            LinearLayout layout = adapter.getRootLayout();
            layout.addView(adapter.getView());


        }

    }
}
